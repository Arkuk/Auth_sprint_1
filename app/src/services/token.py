from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask import jsonify


class TokenService:
    def create_tokens(self):
        # TODO: Надо подумать что хранить внутри токена
        access_token = create_access_token(identity="example_user", fresh=True)
        refresh_token = create_refresh_token(identity="example_user")
        return jsonify(access_token=access_token, refresh_token=refresh_token)

    def refresh_tokens(self):
        """Обновление токена"""
        pass

    def validate_token(self):
        """Првоерка токена"""

    def delete_tokens(self):
        """Удаление токенов"""


token_service = TokenService()
