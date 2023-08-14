def is_prime(number):
    if number <= 1:
        return False
    lower_prime = 2
    while lower_prime < number:
        if number % lower_prime == 0:
            return False
        lower_prime += 1
    return True
