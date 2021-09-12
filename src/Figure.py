

class Figure:
    name = 'Figure'

    def __init__(self, a, b=None, c=None, ):
        self.a: int = a
        self.b: int = b
        self.c: int = c

    def add_area(self, arg):
        if not isinstance(arg, Figure):
            raise ValueError("Не наследуется от класса Figure")
