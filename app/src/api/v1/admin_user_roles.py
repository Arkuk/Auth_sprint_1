from flask_restx import Namespace, Resource
from flask_restx._http import HTTPStatus

from services.user_roles import user_roles
from schemas.user_roles import user_roles_schema_response, assign_role_schema

api = Namespace('API для управления доступами. Управляение ролями пользователей')

user_roles_schema_response = api.model('UserRoleResponse', user_roles_schema_response)
assign_role_schema = api.model('UserRoleResponse', assign_role_schema)

@api.route('/user/roles')
class Roles(Resource):

    @api.marshal_with(user_roles_schema_response, code=int(HTTPStatus.OK))
    def get(self):
        roles = user_roles.get_user_roles(api.payload)
        return roles

    @api.marshal_with(assign_role_schema, code=int(HTTPStatus.CREATED))
    def post(self):
        roles = user_roles.assign_role(api.payload)
        return roles

    @api.marshal_with(assign_role_schema, code=int(HTTPStatus.OK))
    def delete(self):
        roles = user_roles.discard_role(api.payload)
        return roles
