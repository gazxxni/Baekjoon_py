arr = list(map(int, input().split()))
ans = 4

while True:
    cnt = 0
    
    for i in arr:
        if ans % i == 0:
            cnt += 1
    
    if cnt >= 3:
        print(ans)
        break
    
    ans += 1