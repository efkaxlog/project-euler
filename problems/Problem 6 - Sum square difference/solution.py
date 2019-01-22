def solution():
    x = sum(i for i in range(1, 101))
    y = sum(i**2 for i in range(1,101))
    return (x**2 - y)

if __name__ == "__main__":
    print(solution())
