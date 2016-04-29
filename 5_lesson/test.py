#!/usr/bin/python3


class Figure:

        def __init__(self, x, y):

            self.x = x
            self.y = y

        def move(self, x, y):

            self.x += x
            self.y += y

        def __str__(self):
            return '{}: {}, {}'.format(self.__class__.verbose_name, self.x, self.y)


class Rect(Figure):

    verbose_name = 'Прямоугольник'

    def __init__(self, x, y, width, height):

        super(Rect, self).__init__(x, y)

        self.height = height
        self.width = width

    def get_area(self):
        return self.width * self.height


class Circle(Figure):

    verbose_name = 'Круг'

    def __init__(self, x, y, radius):

        super(Circle, self).__init__(x, y)

        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2


circle_1 = Circle(10, 10, 50)
circle_1.move(10, 10)
print(circle_1)


rect_1 = Rect(10, 20, 200, 30)
print(rect_1.get_area())

