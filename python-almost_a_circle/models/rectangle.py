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
        self.width = width
        self.height = height
        self.x = x
        self.y = y 
        """Call the parent class constructor"""
        super().__init__(id)

    @property
    def width(self):
            """accessing width property"""
            return self.__width
    @width.setter
    def width(self, value):
            """set wiidth"""
            if type(value) is not int:
                   raise TypeError("width must be an integer")
            if value <= 0:
                   raise ValueError("width must be > 0")
            self.__width = value                 
            
    @property
    def height(self):
            """accessing height"""
            return self.__height
    @height.setter
    def height(self, value):      
            """setting heigth"""
            if type(value) is not int:
                   raise TypeError("height must be an integer")
            if value <= 0:
                   raise ValueError("height must be > 0")       
            self.__height = value

    @property
    def x(self):
            """accessing x"""
            return self.__x
    @x.setter
    def x(self, value):
            """set x"""
            if type(value) is not int:
                   raise TypeError("x must be an integer")
            if value < 0:
                   raise ValueError("x must be >= 0")
            self.__x = value

    @property
    def y(self):
            """access y"""
            return self.__y
    @y.setter
    def y(self, value):
            """retrieve y"""
            if type(value) is not int:
                   raise TypeError("y must be an integer")
            if value < 0:
                   raise ValueError("y must be >= 0")
            self.__y = value
    def area(self):
        """Calculates area of a rectangle

        Returns:
            int: area
        """
        return self.__width * self.__height
    def display(self):
           """public method that prints in stdout the Rectangle instance with the character #
            returns:
            prints in stdout #
            """
           for y in range(self.__height):
            print("#" * self.__width)
            """overriding the __str__ method
            returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
    def __str__(self):
          return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    """adding the public method def update(self, *args):
    assigns:
    1st argument should be the id attribute
    2nd argument should be the width attribute
    3rd argument should be the height attribute
    4th argument should be the x attribute
    5th argument should be the y attribute"""
    def update(self, *args):
           """
           1st argument should be the id attribute
           2nd argument should be the width attribute
           3rd argument should be the height attribute
           4th argument should be the x attribute
           5th argument should be the y attribute
           """
           print (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")

    