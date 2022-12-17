from flask_restx import fields

role_schema_created = {
    'name': fields.String(required=True, pattern=r'^(?=.{4,32}$)(?![.-])(?!.*[.]{2})[a-zA-Z0-9.-]+(?<![.])$'),
}

role_schema_response = {
    'id': fields.String(required=True),
    'name': fields.String(required=True),
}