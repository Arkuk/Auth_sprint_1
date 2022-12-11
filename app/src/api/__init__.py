from flask_restx import Api
from api.not_authorized import api as api_not_authorized
from api.authorized import api as api_authorized
from api.admin_users import api as api_admin_users
from api.admin_permissions import api as api_admin_permissions
from api.admin_role_permissions import api as api_admin_role_permissions
from api.admin_user_roles import api as api_admin_user_roles
api = Api(
    version='1.0',
    title='Auth',
    description='Auth for praktikum',
    doc='/swagger',
    prefix='/api/v1',
)

api.add_namespace(api_not_authorized, path='/api/v1')
api.add_namespace(api_authorized, path='/api/v1')
api.add_namespace(api_admin_users, path='/api/v1')
api.add_namespace(api_admin_permissions, path='/api/v1')
api.add_namespace(api_admin_role_permissions, path='/api/v1')
api.add_namespace(api_admin_user_roles, path='/api/v1')
