import sys, math
input = sys.stdin.readline

n = int(input())
i = 1

while i * i < n:
    i += 1

j = math.ceil(n / i)

if 1 <= n <= 4:
    print(4)
else:
    print(2 * (i + j - 2))