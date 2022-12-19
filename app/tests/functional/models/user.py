from pydantic import BaseModel


class User(BaseModel):
    username: str | None = None
    password: str | None = None
    roles: list[str] | None = None
    access_token: str | None = None
    refresh_token: str | None = None
