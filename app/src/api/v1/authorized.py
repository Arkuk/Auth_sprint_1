from flask_restx import Namespace, Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt, get_unverified_jwt_headers
from schemas.token import responses_tokens
from services.auth import auth_service
api = Namespace('API для сайта и личного кабинета. Авторизованные пользователи')

responses_tokens = api.model('Token', responses_tokens)
parser = reqparse.RequestParser()
parser.add_argument('User-Agent', location='headers')

auth_service = auth_service

@api.route('/refresh')
class Refresh(Resource):

    @api.marshal_with(responses_tokens, code=200)
    @jwt_required(refresh=True)
    def post(self):
        jwt = get_jwt()
        user_agent = parser.parse_args()['User-Agent']
        result = auth_service.refresh_token(jwt, user_agent)
        return result




@api.route('/me')
class Me(Resource):

    def get(self):
        pass

    def patch(self):
        pass


@api.route('/login_history')
class Me(Resource):

    def get(self):
        pass


@api.route('/logout')
class Me(Resource):

    def post(self):
        pass
