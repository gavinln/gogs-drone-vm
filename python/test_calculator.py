from calculator import add
from calculator import sub


def test_add():
    assert add(3, 4) == 7


def test_sub():
    assert sub(5, 2) == 3
