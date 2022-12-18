import pytest


@pytest.mark.asyncio
async def test_token_refresh():
    '''получение нового токена'''
    pass

@pytest.mark.asyncio
async def test_user_me():
    '''получение информации о юзере по токену'''
    pass

@pytest.mark.asyncio
async def test_user_notme():
    '''получение информации о юзере, передавая невалидный токен'''
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