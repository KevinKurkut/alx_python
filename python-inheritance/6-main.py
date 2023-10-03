#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle
BaseGeometry = __import__('5-base_geometry').BaseGeometry

print(issubclass(Rectangle, BaseGeometry))