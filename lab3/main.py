from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    rectangle = Rectangle(3, 2, 'grey')
    circle = Circle(5, 'green')
    square = Square(5, 'red')

    print(rectangle)
    print(circle)
    print(square)


if __name__ == "__main__":
    # execute only if run as a script
    main()
