import sys
input = sys.stdin.readline

def prime(n):
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    
    return True

t = int(input())

for _ in range(t):
    a = int(input())
    
    if a <= 2:
        print(2)
    else:
        while True:
            if prime(a):
                print(a)
                break
            a += 1