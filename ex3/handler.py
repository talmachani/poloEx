import json


def normalize_json(data):
    return {item["name"]: item[next((key for key in item.keys() if "Val" in key))] for item in data}


def normalize(event, context):

    res = normalize_json(event)

    response = {
        "statusCode": 200,
        "body": json.dumps(res)
    }

    return response

