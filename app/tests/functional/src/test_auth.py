import http

import pytest
from faker import Faker

from tests.functional.models.user import User

fake = Faker()

"""user = {
    "username": fake.user_name(),
    "password": fake.password()
}"""

user = {"username": "usertester", "password": "123qWe!"}

user = User(**user)


@pytest.mark.asyncio
async def test_register(make_request):
    """регистрация"""
    response = await make_request(
        endpoint="/register",
        http_method="post",
        data={
            "username": user.username,
            "password1": user.password,
            "password2": user.password,
        },
    )
    assert response.status == http.HTTPStatus.CREATED


@pytest.mark.asyncio
async def test_login(make_request):
    """вход в аккаунт"""
    response = await make_request(
        endpoint="/login",
        http_method="post",
        data={
            "username": user.username,
            "password": user.password,
        },
    )
    assert response.status == http.HTTPStatus.OK
    user.access_token = response.body["access_token"]
    user.refresh_token = response.body["refresh_token"]


@pytest.mark.asyncio
async def test_login_wrongpassword(make_request):
    """проверка сценария, при котором пользователь ввел неверный пароль"""
    response = await make_request(
        endpoint="/login",
        http_method="post",
        data={
            "username": user.username,
            "password": "123!",
        },
    )
    assert response.status == http.HTTPStatus.UNAUTHORIZED


@pytest.mark.asyncio
async def test_token_refresh(make_request):
    """проверка получения refresh token"""
    response = await make_request(
        endpoint="/refresh",
        http_method="post",
        headers={"Authorization": f"Bearer {user.refresh_token}"},
    )
    assert response.status == http.HTTPStatus.OK
    user.access_token = response.body["access_token"]
    user.refresh_token = response.body["refresh_token"]


@pytest.mark.asyncio
async def test_user_me(make_request):
    """получение информации о юзере по токену"""
    response = await make_request(
        endpoint="/me",
        http_method="get",
        headers={"Authorization": f"Bearer {user.access_token}"},
    )
    assert response.status == http.HTTPStatus.OK


@pytest.mark.asyncio
async def test_change_password(make_request):
    """изменение пароля"""
    response = await make_request(
        endpoint="/change_password",
        http_method="patch",
        headers={"Authorization": f"Bearer {user.access_token}"},
        data={
            "old_password": user.password,
            "new_password1": "Qwerty1!69",
            "new_password2": "Qwerty1!69",
        },
    )
    assert response.status == http.HTTPStatus.OK
    user.password = "Qwerty1!69"


@pytest.mark.asyncio
async def test_login_history(make_request):
    """просмотр истории входа"""
    response = await make_request(
        endpoint="/login_history",
        http_method="get",
        headers={"Authorization": f"Bearer {user.access_token}"},
    )
    assert response.status == http.HTTPStatus.OK


@pytest.mark.asyncio
async def test_logout_access_token(make_request):
    """корректность выхода по access"""
    response = await make_request(
        endpoint="/logout",
        http_method="delete",
        headers={"Authorization": f"Bearer {user.access_token}"},
    )
    assert response.status == http.HTTPStatus.NO_CONTENT


@pytest.mark.asyncio
async def test_logout_refresh_token(make_request):
    """корректность выхода по refresh"""
    response = await make_request(
        endpoint="/logout",
        http_method="delete",
        headers={"Authorization": f"Bearer {user.refresh_token}"},
    )
    assert response.status == http.HTTPStatus.NO_CONTENT
