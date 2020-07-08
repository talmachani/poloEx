from ex2.src.logic import normalize_json


def test_normalize_json():
    data = [
        {
            "name": "device",
            "strVal": "iPhone",
            "metadata": "blalala"
        },
        {
            "name": "isAuthorized",
            "boolVal": "false",
            "metadata": "blalala"
        }
    ]

    res = normalize_json(data)
    assert res == {'device': 'iPhone', 'isAuthorized': 'false'}
