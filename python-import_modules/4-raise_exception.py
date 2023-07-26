def raise_exception():
    raise TypeError("")
try:
    raise_exception()
except TypeError as et:
    print("Exception raised")


              