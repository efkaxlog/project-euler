def solution():
    max_pal = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            num = x * y
            if num > max_pal and str(num) == str(num)[::-1]:
                max_pal = num

    return max_pal

if __name__ == "__main__":
    print(solution())



            
        
