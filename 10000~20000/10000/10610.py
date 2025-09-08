import sys
input = sys.stdin.readline

n = list(input().rstrip())
cnt = 0
arr = []

for i in n:
    arr.append(int(i))

if 0 in arr:
    
    for i in arr:
        cnt += i
        
    if cnt % 3 == 0:
        arr.sort(reverse=True)
        
        print(*arr, sep='')
        
    else:
        print(-1)
    
    
else:
    print(-1)