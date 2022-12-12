from flask_restx import Namespace, Resource

api = Namespace('API для управления доступами. Связь юзера и его ролей')


@api.route('/users/{user_id}/roles')
class RolePermissions(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
