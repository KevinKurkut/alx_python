"""using the Base class
in our rectangle"""
from models.base import Base
"""First Rectangle"""
class Rectangle(Base):
    """Private instance attributes
    Class constructor: 
   args:
    self, width, height, x=0, y=0, id=None """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y 
        """Call the parent class constructor"""
        super().__init__(id)

    @property
    def width(self):
            """accessing width property"""
            return self.__width
    @width.setter
    def width(self, value):
            """set wiidth"""
            self.__width = value
    @property
    def height(self):
            """accessing height"""
            return self.__height
    @height.setter
    def height(self, value):        
            """setting heigth"""
            self.__height = value

    @property
    def x(self):
            """accessing x"""
            return self.__x
    @x.setter
    def x(self, value):
            """set x"""
            self.__x = value

    @property
    def y(self):
            """access y"""
            return self.__y
    @y.setter
    def y(self, value):
            """access y"""
            self.__y = value
