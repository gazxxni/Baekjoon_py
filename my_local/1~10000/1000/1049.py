n,m = map(int,input().split())

arr = []
brr = []

for _ in range(m):
    a, b = map(int, input().split())
    arr.append(int(a))
    brr.append(int(b))

aa = min(arr)
bb = min(brr)

if aa < bb * 6:
    if aa < (n % 6) * bb:
        print((n // 6) * aa + aa)
    else:
        print((n // 6) * aa + (n % 6) * bb)

elif aa >= bb * 6:
    print(n * bb)