import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = bag[i - 1]  # 현재 물건의 무게와 가치
    for j in range(k + 1):
        if j >= w:  # 물건을 넣을 경우와 넣지 않을 경우 비교
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:  # 물건을 넣을 수 없는 경우, 이전 값 그대로 유지
            dp[i][j] = dp[i - 1][j] 

print(dp[n][k])  # 최종 결과 출력
