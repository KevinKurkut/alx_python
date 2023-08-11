"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle
"""class Square"""
class Square(Rectangle):
    """Call the super class with id, x, y, width and height - 
    this super call will use the logic of the __init__ of the Rectangle class.
      The width and height must be assigned to the value of size"""
    def __init__(self, size, x=0, y=0, id=None):
        """inheriting the properties of parent class"""
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
        self.x = x
        self.y = y
    """defining getter method"""
    @property
    def size(self):
        return self.width
    """access width value"""
    @size.setter
    def size(self, value):
         if type(value) is not int:
                   raise TypeError("size must be an integer")
         
         if value < 0:
                   raise ValueError("size must be >= 0")
         self.__width = value
         self.height = value
    """overding str method"""
    def __str__(self):
        '''Overloading string method.'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
        
        
        
