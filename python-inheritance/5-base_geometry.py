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
        