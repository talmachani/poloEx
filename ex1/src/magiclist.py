from dataclasses import dataclass


@dataclass
class Person:
    name: str = None
    age: int = None


class MagicList(list):

    def __init__(self, cls_type=None):
        super().__init__()
        self.cls_type = cls_type

    def __getitem__(self, item):
        if len(self) == item and self.cls_type is not None:
            self.append(self.cls_type())
        return super(MagicList, self).__getitem__(item)

    def __setitem__(self, key, value):
        if key > len(self):
            raise IndexError("list index out of range")
        self.append(value)
