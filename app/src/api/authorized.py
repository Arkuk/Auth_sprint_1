from flask_restx import Namespace, Resource

from schemas.token import responses_tokens

api = Namespace('API для сайта и личного кабинета. Авторизованные пользователи')

responses_tokens = api.model('Token', responses_tokens)


@api.route('/refresh')
class Refresh(Resource):

    @api.marshal_with(responses_tokens, code=200)
    def post(self):
        return api.payload, 201


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
