import sys

n=int(input())
idx=2

while True:
    if (n == 1 or n == 2):
        print(n)
        break
    idx *= 2
    if (idx >= n):
        print((n - (idx // 2)) * 2)
        break
