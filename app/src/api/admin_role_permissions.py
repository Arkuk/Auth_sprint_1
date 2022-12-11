from flask_restx import Namespace, Resource

api = Namespace('API для управления доступами. Связь роли и прав')


@api.route('/roles/{role_id}/permissions')
class RolePermissions(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass
