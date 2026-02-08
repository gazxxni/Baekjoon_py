n = int(input())

consult = []
for i  in range(n):
    t, p = map(int, input().split())
    if i + t > n:
        consult.append((0, 0))
    else:
        consult.append((t, p))

dp = [0 for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    if i + consult[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + consult[i][0]] + consult[i][1])
        
print(dp[0])