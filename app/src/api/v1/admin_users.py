from flask_restx import Namespace, Resource
from flask_restx._http import HTTPStatus

from services.admin import admin_service
from schemas.user import user_schema_response

api = Namespace('API для управления доступами. Юзеры')

users = api.model('Users', user_schema_response)

@api.route('/users')
class User(Resource):
    @api.marshal_with(users, code=HTTPStatus.OK)

    def get(self):
        result = admin_service.get_list_data()
        return result
