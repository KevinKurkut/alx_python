def safe_print_division(a, b):
    a=24
    b=0
   
    try:
        result = safe_print_division(a, b)
    except ZeroDivisionError:
        result = None
        print("Inside result: ".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
    finally:
        print("Inside result: ".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
       

  