import sys
input = sys.stdin.readline

n = int(input())
arr = []
size = []

for i in range(n):
    r, c = map(int, input().split())
    
    if i == 0:
        size.append(r)
        
    size.append(c)
    
dp = [[0] * n for _ in range(n)]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        
        for k in range(i, j):
            c = dp[i][k] + dp[k + 1][j] + size[i] * size[k + 1] * size[j + 1]
            dp[i][j] = min(dp[i][j], c)
            
print(dp[0][n - 1])