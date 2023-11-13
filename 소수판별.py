import math

def is_prime_sqrt(x):
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return 'not prime'
        else:
            return 'prime'