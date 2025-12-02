import sys
import math

# 입력 처리 (H와 Y는 이미 정수)
H, Y = map(int, sys.stdin.read().split())

dp = [0] * (Y + 1)
dp[0] = H

# 투자 옵션 정보: (기간 j, 최종 금액 비율 k * 100)
# 예: 1.05 -> 105
investments_ratio = [
    (1, 105),
    (3, 120),
    (5, 135)
]

# 1년부터 Y년까지 최대 금액을 계산합니다.
for i in range(1, Y + 1):
    for j, ratio in investments_ratio:
        if i >= j:
            principal = dp[i - j]
            
            # 1. 최종 금액을 정수 연산으로 계산합니다.
            # (principal * ratio) // 100: 곱셈 후 나눗셈(//) 연산을 통해 소수점 버림 처리
            final_amount = (principal * ratio) // 100
            
            # 2. DP 갱신
            dp[i] = max(dp[i], final_amount)

print(dp[Y])