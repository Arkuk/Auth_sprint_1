from db.postgres import db
from models.user import User
from models.user_login_history import UserLoginHistory
from sqlalchemy.exc import NoResultFound
from flask_restx import abort
from flask_restx._http import HTTPStatus


class UserService:
    def get_detail_user(self, user_id):
        try:
            user = db.session.execute(db.select(User).filter_by(id=user_id)).one()
            return user[0]
        except NoResultFound:
            abort(HTTPStatus.NOT_FOUND, 'Not found')

    def get_login_history(self, user_id):
        try:
            user_history_login = db.session.execute(db.select(UserLoginHistory).filter_by(user_id=user_id)).all()
            return [item[0] for item in user_history_login]
        except NoResultFound:
            abort(HTTPStatus.NOT_FOUND, 'Not found')


user_service = UserService()
