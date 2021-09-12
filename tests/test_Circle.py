from src.Circle import Circle
from src.Triangle import Triangle
from math import pi


def test_atribut_class():
    assert Circle.name == 'Circle'


def test_perimeter():
    assert Circle(10).perimeter() == 10 * pi * 2


def test_add_area():
    circle1 = Circle(2)
    circle2 = Circle(4)
    triangle = Triangle(2, 2, 2)
    assert circle1.add_area(circle2) == (pi * 2 * 2) + (pi * 4 * 4)
    assert circle2.add_area(triangle) == (pi * 4 * 4) + 3.0


def test_area():
    assert Circle(10).area() == pi * 10 * 10
