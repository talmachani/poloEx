import json
from dataclasses import dataclass

from sanic import Sanic, response
from sanic_jwt import exceptions
from sanic_jwt import Initialize, protected

from ex2.src.db import UserDB
from ex2.src.logic import normalize_json

user_db = UserDB()


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    return await user_db.authenticate(username=username, password=password)


async def retrieve_user_secret(user_id):
    print(f"{user_id}")
    return f"user_id|{user_id}"


app = Sanic(__name__)
Initialize(app, authenticate=authenticate)


@app.route("/")
@protected()
async def protected(request):
    body = json.loads(request.body)
    res = normalize_json(body)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
