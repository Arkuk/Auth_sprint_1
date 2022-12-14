from flask_restx import Namespace, Resource
from services.roles import role_service

api = Namespace('API для управления доступами. Связь юзера и его ролей')


@api.route('/users/{user_id}/roles')
class Roles(Resource):
    def get(self):
        user_id = '00aa5956-bd2d-4478-b8a7-9f25b1a0516c'
        roles = role_service.get_roles(user_id=user_id)
        return roles

    def post(self):
        pass

    def delete(self):
        pass
