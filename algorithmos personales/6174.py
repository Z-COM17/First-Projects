def kapreskar(num):
    for i in range(8):
        num = str(num).replace("", " ").split()   
        while len(num) < 4:
            num.append("0")
        min_num = max_num = ""
        for i in range(len(num)):
            num.sort()    
            min_num += num[i]
            num.sort(reverse = True)
            max_num += num[i]
        num = int(max_num) - int(min_num)
        if num == 6174:
            print(f"We achieved the number 6174 in {i + 1} itenarations")
            return num
    raise IndexError


while True:
    try:
        num = int(input("Enter a number lower than 10000, enter 0 to exit: "))
        if num == 0:
            break
        kapreskar(num)
    except (ValueError, IndexError):
        print("invalid input, try again...")