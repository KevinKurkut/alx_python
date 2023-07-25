def safe_print_division(a, b):
    a = 12
    b = 0
    result = safe_print_division(a, b)
    try:
        a / b
    except:
         if a or b ==0:
             print("Inside result: {}".format(None))
         else:
             print("Inside result: {}".format(result))
    finally:
        print("{:d} / {:d} = {}".format(a, b, result))
                   