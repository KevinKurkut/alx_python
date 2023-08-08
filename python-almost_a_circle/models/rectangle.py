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
        """Private instance attributes"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y 
        """Call the parent class constructor"""
        super().__init__(id)
        """Private instance attributes, each with its own public getter and 
          with its own public setter"""
        @property
        def width(self):
          return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
           return self.__height

        @height.setter
        def height(self, value):
           self.__height = value
        
        @property
        def x(self):
         return self.__x
        
        @x.setter
        def x(self, value):
           self.__x = value
        
        @property
        def y(self):
           return self.__y
        
        @y.setter
        def y(self, value):
           self.__y = value
           