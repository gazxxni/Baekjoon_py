import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr.pop() 
l_arr = len(arr)

INF = float('inf')
dp = [[[INF]*5 for _ in range(5)] for _ in range(2)]
dp[0][0][0] = 0

def move_cost(from_pos, to_pos):
    if from_pos == to_pos:
        return 1
    if from_pos == 0:
        return 2
    if abs(from_pos - to_pos) == 2: 
        return 4
    return 3

for i in range(l_arr):
    cur = i % 2
    nxt = (i + 1) % 2

    for l in range(5):
        for r in range(5):
            dp[nxt][l][r] = INF
    target = arr[i]
    for l in range(5):
        for r in range(5):
            if dp[cur][l][r] == INF:
                continue

            if target != r:
                cost = dp[cur][l][r] + move_cost(l, target)
                dp[nxt][target][r] = min(dp[nxt][target][r], cost)

            if target != l:
                cost = dp[cur][l][r] + move_cost(r, target)
                dp[nxt][l][target] = min(dp[nxt][l][target], cost)

ans = INF
for l in range(5):
    for r in range(5):
        ans = min(ans, dp[l_arr%2][l][r])

print(ans)
