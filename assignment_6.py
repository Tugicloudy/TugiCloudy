from abc import abstractmethod, ABCMeta

class Shape():

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "{:s} color {:s}".format(self.__class__.__name__, self.color)

    def __repr__(self):
        return self.__str__()

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


class TwoDShape(Shape, metaclass=ABCMeta):

    def __str__(self):
        return "{:s} perimeter {:.2f} area {:.2f}".format(super().__str__(), self.get_perimeter(), self.get_area())

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


class Rectangle(TwoDShape):

    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def __str__(self):
        return "{:s} length {:.2f} width {:.2f}".format(
            super().__str__(), self.length, self.width)

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width


def main():
    r1 = Rectangle("red", 2, 5)
    r2 = Rectangle("purple", 3, 3)

    print(r1)
    print(r2)

    list_of_shapes = []
    list_of_shapes.append(r1)
    list_of_shapes.append(r2)
    print(list_of_shapes)

main()