import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque()
log = []

for _ in range(n):
    a = input().split()
    n = int(a[0])
    
    if n == 1:
        c = a[1]
        q.append(c)
        log.append(1)
        
    elif n == 2:
        c = a[1]
        q.appendleft(c)
        log.append(2)
        
    else:
        if log:
            k = log.pop()
            
            if k == 1:
                q.pop()
            else:
                q.popleft()
    
    
if not q:
    print(0)
else:
    print(*q, sep='')