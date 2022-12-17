from flask_restx import fields

user_roles_schema_response = {
    'role_id': fields.String(required=True),
}

assign_role_schema = {
    'user_id': fields.String(required=True),
    'role_id': fields.String(required=True),
}
