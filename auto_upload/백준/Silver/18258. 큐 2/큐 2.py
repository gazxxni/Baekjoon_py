import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    command = input().split()
    
    a = command[0]
    
    if a == 'push':
        b = int(command[1])
        q.append(b)
        
    elif a == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
            
    elif a == 'size':
        print(len(q))
        
    elif a == 'empty':
        if not q:
            print(1)
        else:
            print(0)
            
    elif a == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
            
    elif a == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)