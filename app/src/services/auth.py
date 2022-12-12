from flask_restx import abort
from flask_restx._http import HTTPStatus
from db.postgres import db
from models.user import User


class AuthService:

    def __init__(self):
        abort_text = ''

    def password_comparison(self,
                            password1: str,
                            password2: str):
        """Сравнение паролей"""
        if password1 == password2:
            return True
        return False

    def check_username(self, username: str):
        """Проверка username на наличие в базе"""
        user = db.session.execute(db.select(User).filter_by(username=username)).one()
        print(user)

    def create_user(self, body: dict):
        """Создание юзера"""
        username = body['username']
        password1 = body['password1']
        password2 = body['password2']
        if self.password_comparison(password1, password2):
            self.check_username(username)
        else:
            abort(HTTPStatus.CONFLICT, 'Passwords dont match')

    def login_user(self):
        pass

    def logout_user(self):
        pass


auth_service = AuthService()
