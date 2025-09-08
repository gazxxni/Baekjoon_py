import sys
input = sys.stdin.readline 

t = int(input()) 

for _ in range(t):
    n = int(input())  
    arr = [list(map(int, input().split())) for _ in range(2)]  

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = arr[0][0] 
    dp[1][0] = arr[1][0]  

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = arr[0][1] + arr[1][0]  # 두 번째 열에서 위쪽 + 아래쪽 첫 번째 칸과 더함
    dp[1][1] = arr[1][1] + arr[0][0]  # 두 번째 열에서 아래쪽 + 위쪽 첫 번째 칸과 더함

    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, n):
        # 이전 대각선 값(dp[1][i-1]) 또는 두 칸 전 대각선 값(dp[1][i-2]) 중 최댓값을 더함
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i]

        # 이전 대각선 값(dp[0][i-1]) 또는 두 칸 전 대각선 값(dp[0][i-2]) 중 최댓값을 더함
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i]

    print(max(dp[0][n - 1], dp[1][n - 1]))






"""
arr -> O(n)
dp -> O(n)
for문 -> O(n)
"""