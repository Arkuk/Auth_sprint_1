import os

from dotenv import load_dotenv

load_dotenv()


class Settings(object):
    SQLALCHEMY_DATABASE_URI = f'postgresql:' \
                              f'//{os.getenv("AUTH_POSTGRES_USER")}:' \
                              f'{os.getenv("AUTH_POSTGRES_PASSWORD")}@' \
                              f'localhost:{os.getenv("AUTH_POSTGRES_PORT")}/' \
                              f'{os.getenv("AUTH_POSTGRES_NAME")}'

