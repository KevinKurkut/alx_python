#!/usr/bin/python3
"""
create a square class
"""
Rectangle = __import__('6-rectangle').Rectangle
class Square(Rectangle):
    """Square that inherits from Rectangle"""
    def __init__(self, size):
        """validate using integer validator"""
        self.integer_validator("size", size)
        self.__size = size
    def __str__(self):
        return super().__str__()
        """calculate area of Square"""
    def area(self):
        return self.__size ** 2
