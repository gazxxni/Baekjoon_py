import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 누적 합 배열 생성
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

for _ in range(m):
    a, b = map(int, input().split())
    # a-1부터 b-1까지의 합은 prefix_sum[b] - prefix_sum[a-1]
    ans = prefix_sum[b] - prefix_sum[a - 1]
    print(ans)

