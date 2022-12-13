from datetime import timedelta
import os

from dotenv import load_dotenv

load_dotenv()


class Settings(object):
    SQLALCHEMY_DATABASE_URI = f'postgresql:' \
                              f'//{os.getenv("AUTH_POSTGRES_USER")}:' \
                              f'{os.getenv("AUTH_POSTGRES_PASSWORD")}@' \
                              f'localhost:{os.getenv("AUTH_POSTGRES_PORT")}/' \
                              f'{os.getenv("AUTH_POSTGRES_NAME")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_TOKEN_LOCATION = 'headers'
    JWT_SECRET_KEY = 'super-secret'  # Change this!
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


