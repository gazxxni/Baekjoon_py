import sys

n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
      




# n=int(input())
# stack=[]

# def push(a):
#     a=int(input())
#     stack.append(a)

# def pop():
#     stack.pop(-1)
#     print(stack(-1))

# def size():
#     print(size(stack))

# def empty():
#     if stack == null:
#         print("1")
#     else:
#         print("0")

# def top():
#     if stack[-1] != null:
#         print(stack[-1])
#     else:
#         print("-1")

# for i in range(n):
#     str=input()