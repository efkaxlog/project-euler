import math

def is_prime(num):
    if num > 1:
        sqrt_num = int(math.sqrt(num))
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                return False
        return True
