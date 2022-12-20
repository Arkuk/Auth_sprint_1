from dataclasses import dataclass
from http.client import HTTPResponse

import aiohttp
import pytest
from aiohttp import ClientSession
from multidict import CIMultiDictProxy

from tests.functional.settings import test_settings


@dataclass
class HTTPResponse:
    body: dict
    headers: CIMultiDictProxy[str]
    status: int


@pytest.fixture(scope="session")
async def client_session(event_loop):
    session = ClientSession()
    yield session
    await session.close()


@pytest.fixture(scope="session")
def make_request(client_session):
    dispatcher: dict = {
        "get": client_session.get,
        "post": client_session.post,
        "put": client_session.put,
        "delete": client_session.delete,
        "patch": client_session.patch,
    }

    async def inner(
        http_method: str,
        data: dict = {},
        headers: str = None,
        endpoint: str = None,
    ) -> HTTPResponse:
        async with dispatcher.get(http_method)(
            url=f"{test_settings.service_url}/api/v1{endpoint}",
            headers=headers,
            json=data,
        ) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner
