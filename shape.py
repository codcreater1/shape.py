from math import pi

class Shape:
    def __init__(self):
        self.shape_area = 0
        self.shape_circumference = 0

    def get_area(self):
        return self.shape_area

    def get_circumference(self):
        return self.shape_circumference

    def set_area(self, shape_area):
        self.shape_area = shape_area

    def set_circumference(self, shape_circumference):
        self.shape_circumference = shape_circumference

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def display(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        area = pi * self.radius ** 2
        self.set_area(area)

    def calculate_perimeter(self):
        circum_fr = 2 * pi * self.radius
        self.set_circumference(circum_fr)

    def display(self):
        print("----------------------Circle Information--------------------")
        print("Radius:", self.radius)
        print("Area:", self.get_area())
        print("Circumference:", self.get_circumference())


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        self.set_area(area)

    def calculate_perimeter(self):
        circum_fr = 2 * (self.width + self.height)
        self.set_circumference(circum_fr)

    def display(self):
        print("------------------- Rectangle Information--------------------")
        print("Width:", self.width, "Height:", self.height)
        print("Area:", self.get_area())
        print("Circumference:", self.get_circumference())


if __name__ == "__main__":
    circle = Circle(5)
    circle.calculate_area()
    circle.calculate_perimeter()
    circle.display()

    rectangle = Rectangle(4, 6)
    rectangle.calculate_area()
    rectangle.calculate_perimeter()
    rectangle.display()
