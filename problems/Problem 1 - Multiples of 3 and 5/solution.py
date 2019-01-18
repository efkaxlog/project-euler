# First type of approach that came to mind
def solution1():
    total = 0
    for i in range(3, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# An approach using list comprehension
def solution2():
    return sum(x for x in range(1000) if (x %3 == 0 or x % 5 == 0))
