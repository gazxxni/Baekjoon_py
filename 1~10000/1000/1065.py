n = int(input())

cnt = 0
for i in range(1, n + 1):
    a = list(str(i))
    if i < 100:
        cnt += 1  
    elif int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):
        cnt += 1  
        
print(cnt)