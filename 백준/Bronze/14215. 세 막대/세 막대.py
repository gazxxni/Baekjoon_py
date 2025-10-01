a, b, c = map(int, input().split())

a, b, c = sorted((a, b, c))

if a + b <= c:
    print((a + b) * 2 - 1)
    
elif a == b and b == c:
    print(a * 3)
    
else:
    print(a + b + c)