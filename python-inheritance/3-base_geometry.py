"""creating an empty class"""
class BaseGeometry():
    """BaseGeometry class"""

    """overiding default behaviour of the dir() method when printed"""
    def __init__(cls):
        """getting the attributes of parent class not awre of"""
        attributes = super().__init__()
        list_to_return = []
        for attr in attributes:
            if attr in attributes:
                if attr != "__init_subclass__":
                    #append to the list to return
                    list_to_return.append(attr)
            return list_to_return
        