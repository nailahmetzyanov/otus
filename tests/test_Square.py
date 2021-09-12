import pytest
from src.Square import Square
from src.Circle import Circle


def test_create_class():
    square = Square(2)
    assert isinstance(square, Square)
    assert square.a == 2
    assert square.name == "Square"


def test_perimeter():
    assert Square(2, 2).perimeter() == 8


def test_area():
    assert Square(2, 2).area() == 4


def test_add_area():
    square1 = Square(2, 2)
    square2 = Square(3, 3)
    circle1 = Circle(3)
    assert square1.add_area(square2) == 13
    assert square1.add_area(circle1) == 32.27433388230814

    class NotFigura:
        name = 'Not_figura'

    with pytest.raises(ValueError) as er:
        square1.add_area(NotFigura.name)
    assert 'Не наследуется от класса Figure' in str(er)
