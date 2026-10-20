import pytest
import requests


@pytest.fixture
def base_url():
    return "https://httpbin.org"


@pytest.fixture
def session():
    s = requests.Session()
    yield s
    s.close()