import math

def is_prime_sqrt(x):
    if x == 1:
         return False 
    
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    else:
            return True
    
print(is_prime_sqrt(2))