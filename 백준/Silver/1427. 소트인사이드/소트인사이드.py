import sys
input = sys.stdin.readline

n = input().strip()
a = list(map(int, n))
a.sort(reverse=True)
print(*a, sep='')