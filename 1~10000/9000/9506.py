import sys

def aa(n):
    arr = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            arr.append(i)
            if i * i != n:
                arr.append(n // i)
    arr.sort()
    arr.remove(n) 
    return arr

while True:
    n = int(input())
    if n == -1:
        sys.exit()
    
    a = aa(n)
    
    if n == sum(a):
        print(f"{n} = {' + '.join(map(str, a))}")
    else:
        print(f"{n} is NOT perfect.")
