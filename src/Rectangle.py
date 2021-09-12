from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'

    def area(self) -> int:
        return self.a * self.b

    def perimeter(self) -> int:
        return (self.a + self.b) * 2

    def add_area(self, arg) -> int:
        super().add_area(arg)
        return arg.area() + self.area()
