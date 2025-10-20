import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    command = input().split()
    
    a = int(command[0])
    
    if a == 1:
        q.appendleft(command[1])
        
    elif a == 2:
        q.append(command[1])
        
    elif a == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)
            
    elif a == 4:
        if q:
            print(q.pop())
        else:
            print(-1)
            
    elif a == 5:
        print(len(q))
        
    elif a == 6:
        if q:
            print(0)
        else:
            print(1)
            
    elif a == 7:
        if q:
            print(q[0])
        else:
            print(-1)
            
    elif a == 8:
        if q:
            print(q[-1])
        else:
            print(-1)