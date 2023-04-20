import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = 2 * radius
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2

    def area(self):
        area = math.pi * self.radius ** 2
        return area

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def compare(self, other):
        if self.radius > other.radius:
            print('1st won')
        elif self.radius > other.radius:
            print('2nd won')

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            return NotImplemented

    def sort_key(self):
        return self.radius


circles = [Circle(5), Circle(2), Circle(3), Circle(1)]
circles.sort(key=lambda circle: circle.radius)
for circle in circles:
    print(circle)
