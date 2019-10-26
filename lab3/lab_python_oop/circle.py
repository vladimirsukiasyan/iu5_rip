from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math


class Circle(Figure):
    FIGURE = "Круг"

    def __init__(self, radius, color):
        super().__init__(self.FIGURE)
        self._radius = radius
        self._color = Color
        self._color.value = color

    def area(self):
        return math.pi * self._radius ** 2

    def __repr__(self):
        return '{0}: \nRadius = {1} \nColor = {2} \nArea = {3}\n'.format(
            self._name,
            self._radius,
            self._color.value,
            self.area()
        )
