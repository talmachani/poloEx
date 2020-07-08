from dataclasses import asdict, dataclass


@dataclass
class User:
    user_id: str
    username: str
    password: str

    def to_dict(self):
        return asdict(self)