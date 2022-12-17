from flask_restx import Namespace, Resource, reqparse
from flask_restx._http import HTTPStatus
from flask_jwt_extended import get_jwt
from schemas.token import responses_tokens
from services.auth import auth_service
from services.user import user_service
from schemas.user import user_schema_long_response, login_history_schema, change_password_schema

api = Namespace('API для сайта и личного кабинета. Авторизованные пользователи')

user_schema_long_response = api.model('UserSchemaLongResponse', user_schema_long_response)
login_history_schema = api.model('LoginHistorySchema', login_history_schema)
change_password_schema = api.model('ChangePasswordSchema', change_password_schema)

responses_tokens = api.model('ResponsesTokens', responses_tokens)
parser = reqparse.RequestParser()
parser.add_argument('User-Agent', location='headers')


@api.route('/refresh')
class Refresh(Resource):
    @api.response(int(HTTPStatus.UNAUTHORIZED), 'Token is not corrected\n'
                                                'No token')
    @api.response(int(HTTPStatus.UNPROCESSABLE_ENTITY), 'Token is not corrected\n')
    @api.marshal_with(responses_tokens, code=int(HTTPStatus.OK))
    @auth_service.verify_token(refresh=True)
    def post(self):
        jwt = get_jwt()
        # user_agent = parser.parse_args()['User-Agent']
        result = auth_service.refresh_token(jwt)
        return result


@api.route('/me')
class Me(Resource):
    @auth_service.verify_token()
    @api.response(int(HTTPStatus.UNAUTHORIZED), 'Token is not corrected\n'
                                                'No token')
    @api.response(int(HTTPStatus.UNPROCESSABLE_ENTITY), 'Token is not corrected\n')
    @api.marshal_with(user_schema_long_response, code=int(HTTPStatus.OK))
    def get(self):
        jwt = get_jwt()
        user_id = jwt['sub']
        result = user_service.get_detail_user(user_id)
        return result


@api.route('/change_password')
class ChangePassword(Resource):
    @auth_service.verify_token()
    @api.response(int(HTTPStatus.UNAUTHORIZED), 'Token is not corrected\n'
                                                'No token')
    @api.response(int(HTTPStatus.UNPROCESSABLE_ENTITY), 'Token is not corrected\n')
    @api.response(int(HTTPStatus.CONFLICT), 'New passwords dont matches \n'
                                            'Wrong old password')
    @api.response(int(HTTPStatus.BAD_REQUEST), 'Wrong user')
    @api.expect(change_password_schema)
    def patch(self):
        jwt = get_jwt()
        user_id = jwt['sub']
        auth_service.change_password(api.payload, user_id)
        return {"message": "Password changed"}, 200


@api.route('/login_history')
class LoginHistory(Resource):

    @api.response(int(HTTPStatus.UNAUTHORIZED), 'Token is not corrected\n'
                                                'No token')
    @api.response(int(HTTPStatus.UNPROCESSABLE_ENTITY), 'Token is not corrected\n')
    @api.marshal_list_with(login_history_schema, code=int(HTTPStatus.OK))
    @auth_service.verify_token()
    def get(self):
        jwt = get_jwt()
        user_id = jwt['sub']
        result = user_service.get_login_history(user_id)
        return result


# https://flask-jwt-extended.readthedocs.io/en/stable/blocklist_and_token_revoking/#revoking-refresh-tokens
@api.route('/logout')
class Logout(Resource):
    @auth_service.verify_token(verify_type=False)
    @api.response(int(HTTPStatus.NO_CONTENT), 'Access token is exist\n'
                                              'Refresh token is exist')
    @api.response(int(HTTPStatus.UNAUTHORIZED), 'Token is not corrected\n'
                                                'No token')
    @api.response(int(HTTPStatus.UNPROCESSABLE_ENTITY), 'Token is not corrected\n')
    def delete(self):
        jwt = get_jwt()
        jti = jwt['jti']
        ttype = jwt['type']
        result = auth_service.logout_user(jti, ttype)
        return result
