import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    
    a = int(command[0])
    
    if a == 1:
        b = int(command[1])
        stack.append(b)
        
    elif a == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    elif a == 3:
        print(len(stack))
        
    elif a == 4:
        if not stack:
            print(1)
        else:
            print(0)
            
    elif a == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)