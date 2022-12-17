from db.postgres import db
from flask_restx import abort
from models.user import User
from flask_restx._http import HTTPStatus



class AdminService:
    def get_list_data(self):
        users = db.session.query(User.id, User.username).all()
        if users:
            return users
        abort(HTTPStatus.NOT_FOUND, 'Not Found')


admin_service = AdminService()
