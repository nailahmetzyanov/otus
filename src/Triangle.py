from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            pass
        else:
            raise Exception(f"None: {self.name}")

    def area(self) -> float:
        return self.perimeter() / 2

    def perimeter(self) -> int:
        return self.a + self.b + self.c

    def add_area(self, arg) -> int:
        super().add_area(arg)
        return arg.area() + self.area()
