# Initially was stuck on finding an efficient mathematical way to
# solve this without brute-forcing the answer. But this works also.
def solution():
    target = 1000
    for a in range(1, target + 1):
        for b in range(a + 1, target + 1):
            c = target - a - b
            if a*a + b*b == c*c:
                return str(a * b * c)

if __name__ == "__main__":
    print(solution())
