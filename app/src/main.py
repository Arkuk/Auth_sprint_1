from flask import Flask
from db.postgres import db
from flask_migrate import Migrate
from models.user import User
from models.permission import Permission
from models.role import Role
from models.role_permission import RolePermission
from models.user import User
from models.user_login_history import UserLoginHistory
from models.user_role import UserRole

app = Flask(__name__)
migrate = Migrate(app, db)
app.config.from_object('core.config.Settings')
db.init_app(app)



if __name__ == "__main__":
    app.run()