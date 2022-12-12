from flask_restx import abort
from flask_restx._http import HTTPStatus
from db.postgres import db
from models.user import User
from sqlalchemy.exc import NoResultFound
from passlib.hash import argon2


class AuthService:
    def password_comparison(self,
                            password1: str,
                            password2: str):
        """Сравнение паролей"""
        if password1 == password2:
            return True
        return False

    def check_for_duplication(self, username: str):
        """
        Проверка username на наличие в базе
        :return True если нет дубликатов
        :return False если есть дубликат юзернейма
        """
        try:
            db.session.execute(db.select(User).filter_by(username=username)).one()
            return False
        except NoResultFound:
            return True

    def hash_password(self, password: str):
        return argon2.using(rounds=4).hash(password)

    def create_user(self, body: dict):
        """Создание юзера"""
        username = body['username']
        password1 = body['password1']
        password2 = body['password2']
        if self.password_comparison(password1, password2):
            if self.check_for_duplication(username):
                new_user = User(username=username, password=self.hash_password(password1))
                db.session.add(new_user)
                db.session.commit()
                db.session.refresh(new_user)
                return new_user

            else:
                abort(HTTPStatus.CONFLICT, f'Username {username} already exists')
        else:
            abort(HTTPStatus.CONFLICT, 'Passwords dont match')

    def login_user(self):
        pass

    def logout_user(self):
        pass


auth_service = AuthService()
