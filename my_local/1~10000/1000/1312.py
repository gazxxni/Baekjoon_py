a, b, n = map(int, input().split())
num = a % b

for _ in range(n-1):
    num *= 10
    num %= b

print(num * 10 // b)