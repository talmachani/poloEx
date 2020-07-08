
def normalize_json(data):
    return {item["name"]: item[next((key for key in item.keys() if "Val" in key))] for item in data}