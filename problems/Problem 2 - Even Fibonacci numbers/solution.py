def solution():
    total = 0
    last = 1 # The number before fib
    fib = 2 # Current highest number in the sequence
    while fib <= 4000000:
        if fib % 2 == 0:
            total += fib
        last, fib = fib, fib + last
    return total

if __name__ == "__main__":
    print(solution())
