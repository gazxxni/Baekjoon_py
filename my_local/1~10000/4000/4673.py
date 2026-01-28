arr = [True] + [False] * 10000

for number in range(1, 10001):
    while True:
        str_num = str(number)
        new_num = number
        for i in range(len(str_num)):
            new_num += int(str_num[i])

        number = new_num
        
        if number > 10000:
            break
        
        arr[number] = True

for i in range(10001):
    if not arr[i]:
        print(i)