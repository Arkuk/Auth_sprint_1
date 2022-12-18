import pytest
from aiohttp import ClientSession
from tests.functional.settings import test_settings


@pytest.fixture(scope='session')
async def client_session(event_loop):
    session = ClientSession()
    yield session
    await session.close()


@pytest.fixture(scope='session')
def make_request(client_session):
    async def inner(method: str, params: dict = None):
        params = params or {}
        #передалать url, вместо {method} может передавиться id юзера
        url = 'http://{host}:{port}/api/v1/{method}'.format(
            host=test_settings.service_host, port=test_settings.service_port, method=method
        )
        async with client_session.get(url, params=params) as response:
            return {
                'body': await response.json(),
                'status': response.status,
            }

    return inner