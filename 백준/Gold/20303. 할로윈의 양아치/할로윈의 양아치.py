import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
relation = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
    
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    size = 1
    total = candy[v]
    
    for next in relation[v]:
        if not visited[next]:
            sub_size, sub_total = dfs(next)
            size += sub_size
            total += sub_total
            
    return size, total

components = []
for i in range(1, n + 1):
    if not visited[i]:
        comp_size, comp_candy = dfs(i)
        components.append((comp_size, comp_candy))

capacity = k - 1 
dp = [0] * (capacity + 1)

for size, value in components:
    if size > capacity:
        continue
    for w in range(capacity, size - 1, -1):
        dp[w] = max(dp[w], dp[w - size] + value)

print(max(dp))