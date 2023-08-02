#!usr/bin/python3
"""module with a class that defines a square"""
class Square:
    """defining square object
    args:
    size(param
    ) is assumed to be an int"""
    def __init__(self, size=0):
            self.__size = size 
            """private attribute"""
            while type(size) is int:
                  if size < 0:
                        raise ValueError("size must be >= 0")
                  break
            else:           
                raise TypeError("size must be an integer")
    """public instance method takes parameter self and can be accessed both inside and outside class"""
    def area(self):
          """area"""
          return self.__size ** 2
    """using the property method to access the private attribute value"""
    """property to retrieve private attribute; size"""
    @property
    def size(self):
          return self.__size
    @size.setter
    def size(self, value):
          self.__size = value
          """type/value validation"""
          while type(value) is int:
                  if value < 0:
                        raise ValueError("size must be >= 0")
                  break
          else:           
                raise TypeError("size must be an integer")
          """printing a square"""
          """public insance method that prins the stdout the square with the character #"""
          def my_print(self):
                if self.__size ==0:
                      print("")
                      for i in range(0, self.__size):
                            for j in range(0, self.__size):
                                  print("#", end="")
                            print()
                                