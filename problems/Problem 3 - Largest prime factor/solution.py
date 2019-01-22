import sys
sys.path.append("..")
import euler
    
def solution(): 
    num = 600851475143
    x = 2
    while True:
        if euler.is_prime(x) and num % x == 0:
            num /= x
            # found last and largest prime number
            # this will not work for some numbers, todo: find a clean fix
            if num == 1: 
                return x
        else:
            x += 1

if __name__ == "__main__":
    print(solution())
