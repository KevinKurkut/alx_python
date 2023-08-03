"""exact same object function"""
def is_same_class(obj, a_class):
    """returns true if the object is exactly an instance of the specified class otherwise false"""
    if isinstance(obj,a_class):
        return True
    else:
        return False
    