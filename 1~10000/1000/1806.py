import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

st = 0
total = 0
ans = 1e9

for ed in range(n):
    total += arr[ed]

    while total >= s:
        ans = min(ans, ed - st + 1)
        total -= arr[st]
        st += 1

print(ans if ans != 1e9 else 0)
