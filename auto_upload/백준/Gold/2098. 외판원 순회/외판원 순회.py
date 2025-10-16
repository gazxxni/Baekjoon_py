import sys

n = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[-1] * (1 << n) for _ in range(n)]
inf = float('inf')
all_visited = (1 << n) - 1
start_city = 0

def solve(current_city, visited_mask):
    if visited_mask == all_visited:
        return w[current_city][start_city] if w[current_city][start_city] != 0 else inf

    if dp[current_city][visited_mask] != -1:
        return dp[current_city][visited_mask]

    min_cost = inf
    for next_city in range(n):
        if not (visited_mask & (1 << next_city)) and w[current_city][next_city] != 0:
            cost = w[current_city][next_city] + solve(next_city, visited_mask | (1 << next_city))
            min_cost = min(min_cost, cost)

    dp[current_city][visited_mask] = min_cost
    return min_cost

result = solve(start_city, 1 << start_city)

print(result)