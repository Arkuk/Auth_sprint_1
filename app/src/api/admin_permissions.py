from flask_restx import Namespace, Resource

api = Namespace('API для управления доступами. Права')


@api.route('/permissions')
class Permission(Resource):

    def get(self):
        pass

    def post(self):
        pass


@api.route('/permissions/{item_id}')
class PermissionEdit(Resource):

    def put(self, item_id):
        pass

    def delete(self, item_id):
        pass
