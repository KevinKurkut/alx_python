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
        self.___height = height
        self.__x = x
        self.__y = y 
        """Call the parent class constructor"""
        super().__init__()
        """Private instance attributes, each with its own public getter and 
          with its own public setter"""
        @property
        def width(self):
            self.__width = width
        """Private instance attribute with its own public getter"""
        @width.getter
        def width(self, value):
            self.__width = value
        """Private instance attribute with its own public setter"""
        @property
        def height(self):
            self.___height = height
        """Private instance attribute with its own public setter"""
        @height.getter
        def heigth(self, value):
            self.___height = value
        """Private instance attribute with its own public setter"""
        @property
        def x(self):
            self.___x  = x
        """Private instance attribute with its own public setter"""
        @x.getter
        def x(self, value):
            self.___x = value
        """Private instance attribute with its own public setter"""
        @property
        def y(self):
            self.___y = y
        """Private instance attribute with its own public getter"""
        @y.getter
        def y(self, value):
            self.___y = value
            