from flask_restx import Namespace, Resource, reqparse
from flask_restx._http import HTTPStatus
from flask_jwt_extended import get_jwt
from schemas.token import responses_tokens
from services.auth import auth_service

api = Namespace('API для сайта и личного кабинета. Авторизованные пользователи')

responses_tokens = api.model('Token', responses_tokens)
parser = reqparse.RequestParser()
parser.add_argument('User-Agent', location='headers')


@api.route('/refresh')
class Refresh(Resource):
    @api.marshal_with(responses_tokens, code=HTTPStatus.OK)
    @api.response(int(HTTPStatus.UNAUTHORIZED), 'Token is not corrected\n'
                                                'No token')
    @api.response(int(HTTPStatus.UNPROCESSABLE_ENTITY), 'Token is not corrected\n')
    def post(self):
        if auth_service.verify_token(refresh=True):
            jwt = get_jwt()
            # user_agent = parser.parse_args()['User-Agent']
            result = auth_service.refresh_token(jwt)
            return result


@api.route('/me')
class Me(Resource):

    def get(self):
        pass

    def patch(self):
        pass


@api.route('/login_history')
class LoginHistory(Resource):

    def get(self):
        pass

# https://flask-jwt-extended.readthedocs.io/en/stable/blocklist_and_token_revoking/#revoking-refresh-tokens
@api.route('/logout')
class Logout(Resource):
    @api.response(int(HTTPStatus.NO_CONTENT), 'Access token is exist\n'
                                              'Refresh token is exist')
    @api.response(int(HTTPStatus.UNAUTHORIZED), 'Token is not corrected\n'
                                                'No token')
    @api.response(int(HTTPStatus.UNPROCESSABLE_ENTITY), 'Token is not corrected\n')
    def delete(self):
        if auth_service.verify_token(verify_type=False):
            token = get_jwt()
            print(token)
            jti = token['jti']
            ttype = token['type']
            result = auth_service.logout_user(jti, ttype)
            return result
