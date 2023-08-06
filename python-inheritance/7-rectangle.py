"""rectangle"""
"""empty class"""
class parent(type):
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
class BaseGeometry(metaclass = parent):
    """BaseGeometry class"""  
    def __dir__(cls) -> None:
        """get attributes for this class"""
        attributes = super().__dir__()
        """list comprehesion to remove __init_subclass__"""
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    """Public instance method that raises an Exception"""
    def area(self):
        raise Exception("area() is not implemented")
    """Integer validator"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        """"Rectangle class"""
        
class Rectangle(BaseGeometry):
    """inherits all property of base geometry"""
    def __init__(self, width, height):
        """Rectangle class will no longer inherit the parent's __init__() function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        """implementing area method"""
        def area(self):
            return self.__width * self.__height
        """str()"""
        def __str__(self):
            return f"[Rectangle] {self.__width} / {self.__height}"
            