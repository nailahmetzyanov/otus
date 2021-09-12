from math import pi
from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    def area(self) -> float:
        return pi * self.a * self.a

    def perimeter(self) -> float:
        return 2 * pi * self.a

    def add_area(self, arg) -> int:
        super().add_area(arg)
        return arg.area() + self.area()
