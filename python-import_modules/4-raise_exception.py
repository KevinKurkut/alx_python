def raise_exception():        
        try:
          raise_exception()
        except TypeError as te:
              print("Exception raised", te)
              
              