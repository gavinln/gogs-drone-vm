from triangle import hypotenuse

import math


def test_hypotenuse1():
    assert hypotenuse(3, 4) == 5


def test_hypotenuse2():
    x = 23
    y = 15
    h = hypotenuse(x, y)
    assert h > x and h > y
    assert h < x + y


def test_hypotenuse3():
    x = 23
    y = 15
    h = hypotenuse(x, y)
    assert h < x + y


def test_hypotenuse4():
    x = 23
    h = hypotenuse(x, x)
    assert abs(h - x * math.sqrt(2)) < 0.001
