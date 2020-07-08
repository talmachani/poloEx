import pytest

from ex1.src.magiclist import MagicList, Person


def test_magic_list_primitive_type():
    ml = MagicList()
    ml[0] = 1
    assert ml == [1]


def test_magic_list_multiple_assignments():
    ml = MagicList()
    ml[0] = 1
    ml[1] = 2
    assert ml == [1, 2]


def test_magic_list_rise_index_error():
    ml = MagicList()
    with pytest.raises(IndexError):
        ml[1] = 1


def test_magic_list_with_cls_type():
    expected = Person(age=29)
    ml = MagicList(Person)
    ml[0].age = 29
    assert ml[0] == expected

def test_magic_list_with_cls_type_and_nonexistent_attr():
    expected = Person(age=29)
    ml = MagicList(Person)
    ml[0].foo = 29