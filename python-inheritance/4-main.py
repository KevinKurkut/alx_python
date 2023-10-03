#!/usr/bin/python3
Square = __import__('8-square').Square
Rectangle = __import__('7-rectangle').Rectangle

print(issubclass(Square, Rectangle))
