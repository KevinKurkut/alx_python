#!usr/bin/python3
"""module with a class that defines a square"""
class Square:
    """defining square object
    args:
    size(param
    ) is assumed to be an int"""
    def __init__(self, size):
            self.__size = size 
            """private attribute"""
            if type(size) is not int:
            
                  raise TypeError("size must be an integer")
            if size < 0:
                  raise ValueError("size must be >= 0")
            self.___size = size
                  
