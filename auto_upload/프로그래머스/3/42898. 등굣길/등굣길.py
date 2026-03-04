def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * m for _ in range(n)]
    
    for r in range(n):
        for c in range(m):
            if r == 0 and c == 0:
                dp[r][c] = 1
            else:
                if [c+1, r+1] not in puddles:
                    dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % MOD
                    
            
    return dp[n-1][m-1]