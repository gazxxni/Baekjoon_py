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
    """
    정점 v가 속한 연결요소를 DFS로 탐색하여
    요소의 크기(size: 아이 수)와 사탕 총합(total)을 반환한다.
    """
    visited[v] = True
    size = 1
    total = candy[v]
    
    for next in relation[v]:
        if not visited[next]:
            sub_size, sub_total = dfs(next)
            size += sub_size
            total += sub_total
            
    return size, total

# 모든 연결요소를 (요소 크기, 사탕 합) 형태로 수집
components = []
for i in range(1, n + 1):
    if not visited[i]:
        comp_size, comp_candy = dfs(i)
        components.append((comp_size, comp_candy))

# 0/1 배낭 DP 준비
# 울음 인원 합이 K 이상이 되면 들키므로, 선택 가능한 최대 인원 합은 K-1
capacity = k - 1 
dp = [0] * (capacity + 1)

# 각 연결요소는 "한 번만" 선택 가능 → 0/1 배낭
# weight = 요소 크기(아이 수), value = 요소의 사탕 합
for size, value in components:
    if size > capacity:
        continue
    
    for w in range(capacity, size - 1, -1):
        dp[w] = max(dp[w], dp[w - size] + value)

print(max(dp))