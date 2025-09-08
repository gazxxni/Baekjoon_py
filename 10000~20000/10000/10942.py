import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
for i in range(n - 1):
    if board[i] == board[i + 1]:
        dp[i][i + 1] = 1

for i in range(3, n+1):
    for j in range(n - i + 1):
        if board[j] == board[j + i - 1] and dp[j + 1][j + i - 2]:
            dp[j][j + i - 1] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])