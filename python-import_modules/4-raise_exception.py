def raise_exception():
    raise TypeError("eException raised")
try:
    raise_exception()
except TypeError as et:
    print("Exception has been raised")


              