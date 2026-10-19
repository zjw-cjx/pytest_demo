import pytest
import requests


@pytest.fixture
def base_url():
    """准备工作：提供统一的接口地址"""
    return "https://httpbin.org"


@pytest.fixture
def session():
    """准备工作：建立一个会话；yield 后面是收尾工作"""
    s = requests.Session()
    yield s          # 用例在这里执行
    s.close()        # 用例结束后自动关闭会话（收拾桌子）


def test_with_fixture(base_url, session):
    """注意：参数名和 fixture 函数名一模一样，pytest 自动注入"""
    r = session.get(f"{base_url}/get", params={"name": "kimi"})
    assert r.json()["args"]["name"] == "kimi"

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 0, 0),
    (1000000, 1, 1000001),
])
def test_add_many(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize("name", ["kimi", "alice", "zhangsan"])
def test_get_multi_names(base_url, session, name):
    r = session.get(f"{base_url}/get", params={"name": name})
    assert r.json()["args"]["name"] == name