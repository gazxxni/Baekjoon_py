n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
ed = 0
st = 0
while ed < n:
    cur = sum(arr[st:ed+1])
    
    if cur == m:
        cnt += 1
        ed += 1
    elif cur > m:
        st += 1
    else:
        ed += 1
        
print(cnt)