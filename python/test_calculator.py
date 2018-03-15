from calculator import add
from calculator import sub


def test_add():
    assert add(3, 5) == 8


def test_sub():
    assert sub(5, 3) == 2
