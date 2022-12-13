from flask import Flask

from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from db.postgres import db
import models
from api import api
from db.redis import jwt_redis_blocklist

def create_app(config=None):
    app = Flask(__name__)
    # загрузка настроек для Flask
    app.config.from_object('core.config.Settings')
    # батарейка для миграций
    migrate = Migrate(app, db)
    # инициализация дб
    db.init_app(app)
    # инициализация рест апи
    api.init_app(app)
    # инициализация jwt
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
        jti = jwt_payload["jti"]
        token_in_redis = jwt_redis_blocklist.get(jti)
        return token_in_redis is not None

    return app


app = create_app()
