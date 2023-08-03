"""creating an empty class"""
from collections.abc import Iterable


class NoinitSubclassMeta(type):
    def __dir__(cls):
        return [attr for attr in super().__dir__()  if attr != "__ini_subclass__"]

class BaseGeometry(metaclass = NoinitSubclassMeta):
    """BaseGeometry class"""
    def __dir__(cls):
        """removing init_subclass"""
        return [attr for attr in super().__dir__() if attr != "__init_subclass__"]
