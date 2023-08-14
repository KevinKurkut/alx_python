def is_prime(number):
    if number > 1:
        """iterate all numbers till the number"""
        for m in range(2, number):
            if number % m == 0:
                return False #is not prime
            else:
                return True #prime number
    else:
        return False    
            