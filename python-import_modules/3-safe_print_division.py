def safe_print_division(a, b):
   
    try:
        result = (a / b)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
        return result
    
safe_print_division(12, 2)
safe_print_division(12, 0)

     
       

  