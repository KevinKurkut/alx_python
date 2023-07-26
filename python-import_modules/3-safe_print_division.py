def safe_print_division(a, b):
    a=24
    b=0
   
    try:
        result = (a / b)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: ".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
       

  