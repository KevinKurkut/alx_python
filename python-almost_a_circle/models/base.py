"""my first class"""
class Base:
    """private class attribute __nb_objects = 0"""
    __nb_objects = 0
    """class constructor: def __init__(self, id=None):"""
    def __init__(self, id=None):
        """manage id attribute to avoid duplication"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_object
