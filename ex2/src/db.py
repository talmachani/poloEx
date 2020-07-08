import json
from dataclasses import asdict
from pathlib import Path

from sanic_jwt.exceptions import AuthenticationFailed

from ex2.src.models import User


class UserDB:
    def __init__(self):
        self.db_path = Path("./users.json")
        self.__init_db()

    def __init_db(self):
        # init db with users
        with open(self.db_path, "w") as db_file:
            json.dump([asdict(User("uuid", "admin", "admin"))], db_file)

    async def save(self, user: User):
        with open(self.db_path, "a+") as db_file:
            json.dump([asdict(User("uuid", "admin", "admin"))], db_file)

    async def get(self, username):
        with open(self.db_path, "r") as db_file:
            users = json.load(db_file)
        for u in users:
            if u["username"] == username:
                return User(u["user_id"], u["username"], u["password"])

    async def authenticate(self, username, password):
        user = await self.get(username)
        if user is not None and user.password == password:
            return user
        raise AuthenticationFailed("Incorrect username or password, please try again")
