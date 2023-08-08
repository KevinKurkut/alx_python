"""import base.py"""
from base import Base
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
        """Private instance attributes, each with its own public getter and setter"""
        #width setter function
        @property
        def width(self):
            self.__width = width
        #getter function
        @width.getter
        def width(self, value):
            self.__width = value
        #height setter function
        @property
        def height(self):
            self.___height = height
        #getter function
        @height.getter
        def heigth(self, value):
            self.___height = value
        #x setter function
        @property
        def x(self):
            self.___x  = x
        # getter function
        @x.getter
        def x(self, value):
            self.___x = value
        @property
        def y(self):
            self.___y = y
        @y.getter
        def y(self, value):
            self.___y = value
            