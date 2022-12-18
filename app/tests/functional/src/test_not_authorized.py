import pytest


@pytest.mark.asyncio
async def test_register():
    '''регистрация'''
    pass

@pytest.mark.asyncio
async def test_register_userexists():
    '''проверка сценария, при котором такой пользователь уже зарегистрирован'''
    pass

@pytest.mark.asyncio
async def test_login():
    '''вход в аккаунт'''
    pass

@pytest.mark.asyncio
async def test_login_wrongpassword():
    '''проверка сценария, при котором пользователь ввел неверный пароль'''
    pass