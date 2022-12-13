from flask_restx import abort
from flask_restx._http import HTTPStatus
from db.postgres import db
from models.user import User
from models.user_login_history import UserLoginHistory
from sqlalchemy.exc import NoResultFound
from passlib.hash import argon2

from services.token import token_service

token_service = token_service


class AuthService:
    def password_comparison(self,
                            password1: str,
                            password2: str):
        """Сравнение паролей"""
        if password1 == password2:
            return True
        return False

    def check_for_useername_in_base(self, username: str) -> User | bool:
        """
        Проверка username на наличие в базе
        :return True если нет дубликатов
        :return False если есть дубликат юзернейма
        """
        try:
            user = db.session.execute(db.select(User).filter_by(username=username)).one()
            return user[0]
        except NoResultFound:
            return False

    def hash_password(self, password: str) -> str:
        return argon2.using(rounds=4).hash(password)

    def validate_password(self, password: str, hash_password: str) -> bool:
        return argon2.verify(password, hash_password)

    # def get_hash_password_in_base(self, username: str):
    #     try:
    #         user = db.session.execute(db.select(User).filter_by(username=username)).one()
    #         return user[0].password
    #     except NoResultFound:
    #         return False

    def create_user(self, body: dict):
        """Создание юзера"""
        username = body['username']
        password1 = body['password1']
        password2 = body['password2']
        if self.password_comparison(password1, password2):
            if not self.check_for_useername_in_base(username):
                new_user = User(username=username, password=self.hash_password(password1))
                db.session.add(new_user)
                db.session.commit()
                db.session.refresh(new_user)
                return new_user

            else:
                abort(HTTPStatus.CONFLICT, f'Username {username} already exists')
        else:
            abort(HTTPStatus.CONFLICT, 'Passwords dont match')

    def create_record_history(self):
        new_history_record = UserLoginHistory()
        pass

    def login_user(self, body: dict):
        username = body['username']
        password = body['password']
        user_in_base = self.check_for_useername_in_base(username)
        if user_in_base:
            hash_password = user_in_base.password
            if self.validate_password(password, hash_password):
                return token_service.create_tokens()
            else:
                abort(HTTPStatus.UNAUTHORIZED, 'Wrong login or password')
        else:
            abort(HTTPStatus.UNAUTHORIZED, 'Wrong login or password')

    def logout_user(self):
        pass


auth_service = AuthService()
