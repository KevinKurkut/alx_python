#!usr/bin/python3
"""module with a class that defines a square"""
class Square:
    """defining square object
    args:
    size(param
    ) is assumed to be an int"""
    def __init__(self, size):
            self.size = size 
            """private attribute"""
            while type(size) is not int:
                  if size <= 0:
                        raise ValueError("size must be >= 0")
                  break
                  
            else:           
                raise TypeError("size must be an integer")
    """public instance method takes self parameter and can be accessed inside and outside class"""
    def area(self):
          """this is a public instance method"""
          x=Square()
          """creating instance of a class"""
          x.area()
          """calling"""
                  