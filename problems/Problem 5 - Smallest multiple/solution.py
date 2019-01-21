# -- Solution 1 -- (70 seconds execution time)
# Working solution but extremely slow. Brute force.
def solution1():    
    x = 0
    while True:
        x += 1
        found = True # assume found until proven false
        for i in range(2, 21): # start from 2 since dividing by 1 is pointless
            if x % i != 0:
                found = False
                break
        if found:
            break

    return x


# -- Solution 2 -- (25 seconds execution time)
def find_lcm(x, y):
    i = 1
    while True:
        i += 1
        if i % x == 0 and i % y == 0:
            return i
        
# Find answer by finding the least common multiple (lcm) of the first
# two numbers in the sequence, then find the lcm of the result and the
# next number etc. until the end of the sequence.
def solution2():
    num = 1
    for x in range(2, 21):
        num = find_lcm(x, num)
    return num


if __name__ == "__main__":
    print(solution2())
