from flask_restx import abort
from flask_restx._http import HTTPStatus
from db.postgres import db
from db.redis import redis_cache
from models.user import User
from models.user_login_history import UserLoginHistory
from sqlalchemy.exc import NoResultFound
from passlib.hash import argon2
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token


redis_cache = redis_cache


class AuthService:
    def password_comparison(self,
                            password1: str,
                            password2: str):
        """Сравнение паролей"""
        if password1 == password2:
            return True
        return False

    def create_tokens(self, user_id):
        access_token = create_access_token(identity=user_id)
        refresh_token = create_refresh_token(identity=user_id)
        return {'access_token': access_token, 'refresh_token': refresh_token}

    def check_for_id_in_base(self, user_id: str):
        """
        Проверка id на наличие в базе
        """
        try:
            user = db.session.execute(db.select(User).filter_by(id=user_id)).one()
            return user[0]
        except NoResultFound:
            return False

    def check_for_useername_in_base(self, username: str) -> User | bool:
        """
        Проверка username на наличие в базе
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

    def create_record_history(self, user_id, user_agent):
        new_history_record = UserLoginHistory(user_id=user_id, user_agent=user_agent)
        db.session.add(new_history_record)
        db.session.commit()
        return True

    def login_user(self, body: dict, user_agent: str):
        username = body['username']
        password = body['password']
        user_in_base = self.check_for_useername_in_base(username)
        if user_in_base:
            hash_password = user_in_base.password
            if self.validate_password(password, hash_password):
                self.create_record_history(user_in_base.id, user_agent)
                tokens = self.create_tokens(str(user_in_base.id))
                redis_cache.put_data_to_cache(str(user_in_base.id),
                                              user_agent,
                                              tokens['refresh_token'])
                return tokens
            else:
                abort(HTTPStatus.UNAUTHORIZED, 'Wrong login or password')
        else:
            abort(HTTPStatus.UNAUTHORIZED, 'Wrong login or password')

    def refresh_token(self, jwt: dict, user_agent: str):
        user_id = jwt['sub']
        if self.check_for_id_in_base(user_id):
            tokens = self.create_tokens(user_id)
            redis_cache.put_data_to_cache(user_id,
                                          user_agent,
                                          tokens['refresh_token'])
            return tokens



    def logout_user(self):
        pass


auth_service = AuthService()
