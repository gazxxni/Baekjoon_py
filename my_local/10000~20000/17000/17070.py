n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

def solution():

    # 1행은 전부 가로 -> 미리 처리하기
    dp[0][0][1] = 1
    for i in range(2, n):
        if arr[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]
	
    
    # 1행은 전부 가로로 처리, 1열은 전부 세로이지만 세로가 불가능하므로 제외
    for r in range(1, n):
        for c in range(1, n):  # 벽이 있는지 검사
            # 대각선 파이프를 추가하는 과정 
            if arr[r][c] == 0 and arr[r][c - 1] == 0 and arr[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
                
	        # 가로, 세로 파이프를 추가하는 과정
            # 가로는 가로, 대각선일때 / 세로는 세로, 대각선일때
            if arr[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]
    
    print(sum(dp[i][n - 1][n - 1] for i in range(3)))

solution()