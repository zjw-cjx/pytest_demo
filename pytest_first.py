import requests


def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, -2) == -3


class TestGroup:
    def test_zero(self):
        assert add(0, 0) == 0


def test_httpbin_get():
    r = requests.get("https://httpbin.org/get", params={"name": "kimi"})
    assert r.status_code == 200
    assert r.json()["args"]["name"] == "kimi"


def test_httpbin_post():
    r = requests.post("https://httpbin.org/post", json={"age": 18})
    assert r.json()["json"]["age"] == 18


def test_httpbin_header():
    r = requests.get("https://httpbin.org/headers", headers={"Token": "abc123"})
    assert r.json()["headers"]["Token"] == "abc123"