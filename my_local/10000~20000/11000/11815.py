import sys
input = sys.stdin.readline

def search(x):
    r = int(x**0.5)
    
    if r * r == x:
        return True
    else:
        return False

n = int(input().strip())

for _ in range(n):
    arr = list(map(int, input().split()))
    
    for i in arr:
            
        if search(i):
            print(1)
        else:
            print(0)
