from flask_restx import abort
from flask_restx._http import HTTPStatus

from db.postgres import db
from models.user import User


class AdminService:
    def get_list_data(self):
        users = db.session.query(User.id, User.username).all()
        if users:
            return users
        abort(HTTPStatus.NOT_FOUND, "Not Found")


admin_service = AdminService()
