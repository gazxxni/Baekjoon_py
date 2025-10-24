n = int(input())

arr = set()
flag = False
for _ in range(n):
    a = input().rstrip().split()
    b = a[0]
    c = a[1]
    if b == 'ChongChong' or c == 'ChongChong':
        flag = True
        arr.add(b)
        arr.add(c)
    
    if flag:
        if b in arr or c in arr:
            arr.add(b)
            arr.add(c)
    
print(len(arr))