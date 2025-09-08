import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [i for i in range(n+1)] 

cnt = 0
ans = 0

for i in range(2, n + 1):
    
    if arr[i] == 0: 
        continue
    
    for j in range(i, n+1, i):
        
        if arr[j] != 0:
            arr[j] = 0
            cnt += 1
            
            if cnt == k:
                ans = j
                break
        
print(ans)