from flask import Flask

from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from db.postgres import db
import models
from api import api


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
    return app


app = create_app()
