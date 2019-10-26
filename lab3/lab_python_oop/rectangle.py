from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):
    FIGURE = "Прямоугольник"

    def __init__(self, width, height, color):
        super().__init__(self.FIGURE)
        self._width = width
        self._height = height
        self._color = Color
        self._color.value = color

    def area(self):
        return self._width * self._height

    def __repr__(self):
        return '{0}: \nWidth = {1} \nHeight = {2} \nColor = {3} \nArea = {4}\n'.format(
            self._name,
            self._width,
            self._height,
            self._color.value,
            self.area()
        )
