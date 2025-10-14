def primenum(n):
    arr = [True] * (n + 1)
    arr[0] = arr[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False
                
    brr = []
    for i in range(2, n + 1):
        if arr[i]:
            brr.append(i)
            
    return brr

a = primenum(1000000)
b = set(a)
t = int(input())

for _ in range(t):
    n = int(input())

    cnt = 0

    for i in a:
        if i > n // 2:
            break
        
        if (n - i) in b:
            cnt += 1
            
    print(cnt)