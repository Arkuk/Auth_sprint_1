from flask_restx import fields

user_schema_register = {
    'username': fields.String(required=True),
    'password1': fields.String(required=True),
    'password2': fields.String(required=True),
}

user_schema_login = {
    'username': fields.String(required=True),
    'password1': fields.String(required=True),
}