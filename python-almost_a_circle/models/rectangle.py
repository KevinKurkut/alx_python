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
          """accessing width"""
          return self.__width

        """Private instance attributes, each with its own public getter and 
          with its own public setter"""
        @property
        def height(self):
           """accessing height"""
           return self.__height
        