def solution(dartResult):
    num = ''
    arr = []
    for i in dartResult:
        if i.isnumeric():
            num += i
            
        elif i == 'S':
            num = int(num)
            arr.append(num)
            num = ''
            
        elif i == 'D':
            num = int(num) ** 2
            arr.append(num)
            num = ''
            
        elif i == 'T':
            num = int(num) ** 3
            arr.append(num)
            num = ''
            
        elif i == '*':
            if len(arr) > 1:
                arr[-2] = arr[-2] * 2
                arr[-1] = arr[-1] * 2
            else:
                arr[-1] = arr[-1] * 2
                
        elif i == '#':
            arr[-1] = arr[-1] * -1
            
            
    return sum(arr)