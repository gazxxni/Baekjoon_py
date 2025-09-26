x, y, w, h = map(int, input().split())

a = abs(x - w)
b = abs(y - h)
c = abs(x)
d = abs(y)

print(min(a, b, c, d))