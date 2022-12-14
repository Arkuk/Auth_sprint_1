from flask_restx import Namespace, Resource
from services.admin import admin_service

api = Namespace('API для управления доступами. Юзеры')


@api.route('/users')
class User(Resource):

    def get(self):
        result = admin_service.get_list_data()
        return result
