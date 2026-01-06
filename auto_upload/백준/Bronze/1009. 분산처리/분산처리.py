import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    
    base = a % 10
    
    if base == 0:
        print(10)
    elif base in [1, 5, 6]:
        print(base)
    elif base in [4, 9]:
        remain = b % 2
        if remain == 0:
            print((base ** 2) % 10)
        else:
            print(base)
    else:
        remain = b % 4
        if remain == 0:
            print((base ** 4) % 10)
        else:
            print((base ** remain) % 10)