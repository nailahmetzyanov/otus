import pytest
import requests


def pytest_addoption(parser):
    parser.addoption('--url', help='Введите url запроса', default='https://ya.ru/')
    parser.addoption("--status_code", help='Код ответа', default=200)


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption('--url')


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        return requests.get(url=url, params=params, headers=headers)


@pytest.fixture
def api_client(request, url):
    url = request.config.getoption('--url')
    return ApiClient(base_address=url)
