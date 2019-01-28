import sys
sys.path.append("..")
import euler

# Takes a few seconds but works.
def solution():
    return sum(x for x in range(2000000) if euler.is_prime(x))

if __name__ == "__main__":
    print(solution())
