import json
import pytest


def load_data():
    with open("data/names.json", encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.parametrize("case", load_data())
def test_name_from_file(base_url, session, case):
    r = session.get(f"{base_url}/get", params={"name": case["name"]})
    assert r.json()["args"]["name"] == case["expected"]