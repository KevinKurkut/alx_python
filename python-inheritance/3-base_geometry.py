"""creating an empty class"""
class BaseGeometry:
    """BaseGeometry class"""
    
    def __dir__(cls) -> None:
        """get attributes for this class"""
        attributes = super().__dir__()
        """list comprehesion to remove __init_subclass__"""
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
        