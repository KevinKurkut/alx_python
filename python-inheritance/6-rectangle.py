BaseGeometry =__import__('5-base_geometry').BaseGeometry
        
class Rectangle(BaseGeometry):
    """inherits all property of base geometry"""
    def __init__(self, width, height):
        """Rectangle class will no longer inherit the parent's __init__() function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        