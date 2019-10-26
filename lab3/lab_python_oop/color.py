class Color:
    def __init__(self, color):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        pass

    @value.deleter
    def value(self):
        del self._value
