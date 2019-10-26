from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE = "Квадрат"

    def __init__(self, length, color):
        super().__init__(length, length, color)

    def __repr__(self):
        return '{0}: \nLength = {1} \nColor = {2} \nArea = {3}\n\n'.format(
            self._name,
            self._width,
            self._color.value,
            self.area()
        )
