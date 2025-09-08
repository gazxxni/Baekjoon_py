n = int(input())

if n <= 4:
    dp = [0] * 5
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 3
    print(dp[n])
    
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 3
    for i in range(5, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    print(dp[n])