import sys
input = sys.stdin.readline

n = int(input())  
a = list(map(int, input().split()))
dp = [1] * n  

for i in range(1, n):  # i는 현재 위치
    for j in range(i):  # j는 i 이전의 모든 위치
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
