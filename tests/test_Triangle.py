import pytest
from src.Triangle import Triangle
from src.Circle import Circle


def test_create_class():
    triangle = Triangle(2, 4, 3)
    assert isinstance(triangle, Triangle)
    assert triangle.a == 2
    assert triangle.b == 4
    assert triangle.c == 3

    with pytest.raises(Exception) as er:
        Triangle(2, 40, 100)
    assert "None: Triangle" in str(er)


def test_perimeter():
    assert Triangle(2, 4, 3).perimeter() == 9


def test_area():
    assert Triangle(2, 2, 2).area() == 3


def test_add_area():
    triangle1 = Triangle(2, 2, 2)
    triangle2 = Triangle(4, 4, 4)
    circle1 = Circle(3)
    assert triangle1.add_area(triangle2) == 9
    assert triangle1.add_area(circle1) == 31.274333882308138

    class NotFigura:
        name = 'Not_figura'

    with pytest.raises(ValueError) as er:
        triangle1.add_area(NotFigura.name)
    assert 'Не наследуется от класса Figure' in str(er)
