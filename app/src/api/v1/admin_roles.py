from flask_restx import Namespace, Resource, reqparse
from flask_restx._http import HTTPStatus

from schemas.role import role_schema_created, role_schema_response
from services.roles import role_service


api = Namespace('API для сайта и личного кабинета. Управление ролями', validate=True)

role_schema_created = api.model('RoleCreate', role_schema_created)
role_schema_response = api.model('RoleRespose', role_schema_response)


@api.route('/roles')
class RoleCRUD(Resource):

    @api.marshal_with(role_schema_created, code=int(HTTPStatus.CREATED))
    def post(self):
        result = role_service.create_role(api.payload)
        return result, 201

    @api.marshal_with(role_schema_response, code=int(HTTPStatus.OK))
    def get(self):
        result = role_service.get_roles_list()
        return result, 200

    def delete(self):
        result = role_service.delete_role(api.payload)
        return result, 200