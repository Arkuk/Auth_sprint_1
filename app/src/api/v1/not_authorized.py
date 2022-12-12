from flask_restx import Namespace, Resource
from flask_restx._http import HTTPStatus
from schemas.user import user_schema_register, user_schema_login, user_schema_response
from services.auth import auth_service

api = Namespace('API для сайта и личного кабинета. Анонимные пользователи', validate=True)


user_schema_register = api.model('UserSchemaRegister', user_schema_register)
user_schema_login = api.model('UserSchemaLogin', user_schema_login)
user_schema_response = api.model('UserSchemaResponse', user_schema_response)



@api.route('/register')
class Register(Resource):
    @api.expect(user_schema_register)
    @api.marshal_with(user_schema_response, code=201)

    @api.response(int(HTTPStatus.CONFLICT), 'Passwords dont match')
    def post(self):
        auth_service.create_user(api.payload)
        return api.payload, 201


@api.route('/login')
class Login(Resource):
    @api.expect(user_schema_login)
    @api.marshal_with(user_schema_login, code=200)
    def post(self):
        return api.payload, 200
