import sys
input = sys.stdin.readline

c, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [float('inf')] * (c + 100)
dp[0] = 0

for i in range(1, c + 100):
    for cost, people in arr:
        if i - people >= 0:
            dp[i] = min(dp[i], dp[i - people] + cost)

print(min(dp[c:]))