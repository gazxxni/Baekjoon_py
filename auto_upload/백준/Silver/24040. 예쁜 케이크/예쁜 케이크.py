import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    remainder = n % 3
    
    if remainder == 1:
        print('NIE')
    elif remainder == 2:
        print('TAK')
    else:
        if n % 9 == 0:
            print('TAK')
        else:
            print('NIE')