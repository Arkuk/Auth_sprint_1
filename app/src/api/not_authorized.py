from flask_restx import Namespace, Resource
from schemas.user import user_schema_register, user_schema_login

api = Namespace('API для сайта и личного кабинета. Анонимные пользователи')

user_schema_register = api.model('UserSchemaRegister', user_schema_register)
user_schema_login = api.model('UserSchemaLogin', user_schema_login)


@api.route('/register')
class Register(Resource):
    @api.expect(user_schema_register)
    @api.marshal_with(user_schema_register, code=201)
    def post(self):
        return api.payload, 201


@api.route('/login')
class Login(Resource):
    @api.expect(user_schema_login)
    @api.marshal_with(user_schema_login, code=200)
    def post(self):
        return api.payload, 200
