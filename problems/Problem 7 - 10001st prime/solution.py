import sys
sys.path.append("..")
import euler

def solution():
        i = 0
        primes_found = 0
        while primes_found < 10001:
            i += 1
            if euler.is_prime(i):
                primes_found += 1
        return i

if __name__ == "__main__":
    print(solution())
