import json


def normalize_json(data):
    return {item["name"]: item[next((key for key in item.keys() if "Val" in key))] for item in data}


def normalize(event, context):

    data = json.loads(event['body'])
    res = normalize_json(data)

    response = {
        "statusCode": 200,
        "body": json.dumps(res)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
