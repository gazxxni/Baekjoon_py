import sys
input = sys.stdin.readline

a = input().rstrip()
n = len(a)
isPal = [[False] * n for _ in range(n)]

for i in range(n):
    isPal[i][i] = True
    
for i in range(n-1):
    if a[i] == a[i + 1]:
        isPal[i][i + 1] = True

for length in range(3, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        if a[i] == a[j] and isPal[i + 1][j - 1]:
            isPal[i][j] = True
            
dp = [float('inf')] * n

for i in range(n):
    for j in range(i + 1):
        if isPal[j][i]:
            if j == 0:
                dp[i] = 1
            else:
                dp[i] = min(dp[i], dp[j - 1] + 1)


print(dp[n - 1])