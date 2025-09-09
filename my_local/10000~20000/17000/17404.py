import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

result = INF

for first_color in range(3):  # 0: 빨강, 1: 초록, 2: 파랑
    dp = [[INF]*3 for _ in range(n)]
    
    # 1번 집의 색을 고정
    dp[0][first_color] = cost[0][first_color]

    for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])  # 빨강
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])  # 초록
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])  # 파랑

    # 마지막 집의 색이 첫 번째 집의 색과 같지 않은 경우만 고려
    for last_color in range(3):
        if last_color != first_color:
            result = min(result, dp[n-1][last_color])

print(result)
