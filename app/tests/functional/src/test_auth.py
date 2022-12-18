import http

import pytest

@pytest.mark.asyncio
async def test_register(make_request):
    '''регистрация'''
    response = await make_request(
        endpoint="/api/v1/register",
        http_method="post",
        data={
            "username": "Tester",
            "password1": "Qwerty1!",
            "password2": "Qwerty1!",
        },
    )
    assert response.status == http.HTTPStatus.OK #исправить статус в сервисе авторизации, сейчас при регистрации возвращается 200


@pytest.mark.asyncio
async def test_login():
    '''вход в аккаунт'''
    pass

@pytest.mark.asyncio
async def test_login_wrongpassword():
    '''проверка сценария, при котором пользователь ввел неверный пароль'''
    pass

@pytest.mark.asyncio
async def test_token_refresh():
    '''получение нового токена'''
    pass

@pytest.mark.asyncio
async def test_user_me():
    '''получение информации о юзере по токену'''
    pass

@pytest.mark.asyncio
async def test_change_password():
    '''изменение пароля'''
    pass

@pytest.mark.asyncio
async def test_login_history():
    '''просмотр истории входа'''
    pass

@pytest.mark.asyncio
async def test_logout():
    '''корректность выхода'''
    pass