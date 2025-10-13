a, b = map(int, input().split())
c, d = map(int, input().split())

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y / gcd(x, y)

n = lcm(b, d)
aa = n // b
bb = n // d

cc = aa * a + bb * c
dd = gcd(cc, n)
print(int(cc // dd), int(n // dd))