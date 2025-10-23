n = int(input())

def fac(n):
    if n == 1:
        return 1
    
    return n * fac(n - 1)

if n == 0:
    print(1)
else:
    print(fac(n))