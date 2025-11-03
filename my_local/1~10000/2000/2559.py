import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ss = sum(arr[:k])
ans = ss

for i in range(k, n):
    ss = ss - arr[i - k] + arr[i]
    ans = max(ans, ss)

print(ans)