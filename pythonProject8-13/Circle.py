import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__x = 0
        self.__y = 0

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius