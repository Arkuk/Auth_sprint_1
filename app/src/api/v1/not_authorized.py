from flask_restx import Namespace, Resource, reqparse
from flask_restx._http import HTTPStatus
from schemas.user import user_schema_register, user_schema_login, user_schema_response
from schemas.token import responses_tokens
from services.auth import auth_service

api = Namespace('API для сайта и личного кабинета. Анонимные пользователи', validate=True)


user_schema_register = api.model('UserSchemaRegister', user_schema_register)
user_schema_login = api.model('UserSchemaLogin', user_schema_login)
user_schema_response = api.model('UserSchemaResponse', user_schema_response)
responses_tokens = api.model('ResponsesTokens', responses_tokens)

parser = reqparse.RequestParser()
parser.add_argument('User-Agent', location='headers')
parser.add_argument('X-Forwarded-For', location='headers')
parser.add_argument('client-ip-http-header', location='headers')
parser.add_argument('HTTP_CLIENT_IP', location='headers')




@api.route('/register')
class Register(Resource):
    @api.expect(user_schema_register)
    @api.marshal_with(user_schema_response, code=201)
    @api.response(int(HTTPStatus.CONFLICT), 'Passwords dont match \n'
                                            'Username already exits')
    @api.response(int(HTTPStatus.BAD_REQUEST), 'Bad request')
    def post(self):
        result = auth_service.create_user(api.payload)
        return result, 201


@api.route('/login')
class Login(Resource):
    @api.expect(user_schema_login)
    @api.marshal_with(responses_tokens, code=200)
    @api.response(int(HTTPStatus.BAD_REQUEST), 'Wrong login or password')
    def post(self):
        args = parser.parse_args()
        print(args)


        result = auth_service.login_user(api.payload)
        return result.json
