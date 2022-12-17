from flask_restx import Namespace, Resource
from flask_restx._http import HTTPStatus

from services.user_roles import user_roles
from schemas.user_roles import user_roles_schema_response, assign_role_schema

api = Namespace('API для управления доступами. Управляение ролями пользователей')

user_roles_schema_response = api.model('UserRoleResponse', user_roles_schema_response)
assign_role_schema = api.model('UserRoleResponse', assign_role_schema)

@api.route('/<user_id>/roles')
class Roles(Resource):

    @api.marshal_with(user_roles_schema_response, code=int(HTTPStatus.OK))
    def get(self, user_id):
        roles = user_roles.get_user_roles(user_id)
        return roles

    @api.marshal_with(user_roles_schema_response, code=int(HTTPStatus.CREATED))
    def post(self, user_id):
        roles = user_roles.assign_role(user_id, api.payload)
        return roles

    @api.marshal_with(user_roles_schema_response, code=int(HTTPStatus.OK))
    def delete(self, user_id):
        roles = user_roles.discard_role(user_id, api.payload)
        return roles
