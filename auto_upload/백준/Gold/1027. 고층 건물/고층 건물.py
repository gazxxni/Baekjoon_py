n = int(input())
arr = list(map(int, input().split()))\
    
def cal(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

if n == 1:
    print(0)

else:
    ans = 0

    for i in range(n):
        cnt = 0
        cur = float('inf')

        for j in range(i - 1, -1, -1):
            nxt = cal(i, arr[i], j , arr[j])
            
            if nxt < cur:
                cur = nxt
                cnt += 1
                
        cur = -float('inf')
        
        for j in range(i + 1, n):
            nxt = cal(i, arr[i], j, arr[j])
            
            if nxt > cur:
                cur = nxt
                cnt += 1
                
        ans = max(ans, cnt)
        
    print(ans)