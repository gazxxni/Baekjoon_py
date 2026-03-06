def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for r in range(1,n+1):
        for c in range(1,m+1):
            if [c, r] not in puddles:
                dp[r][c] += dp[r-1][c] + dp[r][c-1]
            
    
    
    return dp[n][m] % 1000000007