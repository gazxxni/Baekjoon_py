import sys
input = sys.stdin.readline

MOD = 1_000_000_000
n = int(input())
dp = [[[0] * 1024 for _ in range(10)] for _ in range(n + 1)]

# 길이 1의 계단 수 초기화
for j in range(1, 10):
    dp[1][j][1 << j] = 1

for i in range(1, n):
    for j in range(10):
        for k in range(1 << 10):
            if dp[i][j][k] == 0:
                continue
            
            # Case 1: 다음 숫자가 j-1일 경우
            if j > 0:
                new_digit = j - 1
                new_mask = k | (1 << new_digit)
                dp[i + 1][new_digit][new_mask] = (dp[i + 1][new_digit][new_mask] + dp[i][j][k]) % MOD
            
            # Case 2: 다음 숫자가 j+1일 경우
            if j < 9:
                new_digit = j + 1
                new_mask = k | (1 << new_digit)
                dp[i + 1][new_digit][new_mask] = (dp[i + 1][new_digit][new_mask] + dp[i][j][k]) % MOD

result = 0
for j in range(10):
    result = (result + dp[n][j][(1 << 10) - 1]) % MOD
    
print(result)