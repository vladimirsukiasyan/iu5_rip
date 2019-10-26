from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @property
    def name(self):
        return self._name
