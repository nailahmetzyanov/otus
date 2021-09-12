import pytest
from src.Rectangle import Rectangle
from src.Circle import Circle


def test_create_class():
    rectangle = Rectangle(2, 4)
    assert isinstance(rectangle, Rectangle)
    assert rectangle.a == 2
    assert rectangle.b == 4
    assert Rectangle.name == 'Rectangle'


def test_perimeter():
    assert Rectangle(2, 4).perimeter() == 12


def test_area():
    assert Rectangle(2, 4).area() == 8


def test_add_area():
    rectangle1 = Rectangle(2, 4)
    rectangle2 = Rectangle(3, 6)
    circle1 = Circle(5)
    assert rectangle1.add_area(rectangle2) == 26
    assert str(rectangle1.add_area(circle1))[:-12] == str(86.53)

    class NotFigura:
        name = 'Not_figura'

    with pytest.raises(ValueError) as er:
        rectangle1.add_area(NotFigura.name)
    assert 'Не наследуется от класса Figure' in str(er)
