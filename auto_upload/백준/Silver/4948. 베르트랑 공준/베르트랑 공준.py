def prime_numbers(n):
    arr = [True] * (n + 1) 
    arr[0] = arr[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False
    
    return arr

a = prime_numbers(300000)

while True:
    n = int(input())
    
    if n == 0:
        exit()
        
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if a[i] == True:
            cnt += 1
    
    print(cnt)