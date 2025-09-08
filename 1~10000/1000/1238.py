import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
arr = [[] for _ in range(n + 1)]
brr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    arr[a].append((b, t))
    brr[b].append((a, t))

def dijk(st, arr, n):
    q = []
    heapq.heappush(q, (0, st))
    dist = [INF] * (n + 1)
    dist[st] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue

        for i in arr[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return dist 

# 역방향 그래프를 구성해 총 2번의 다익스트라를 수행    
fromX = dijk(x, arr, n)  # x에서 각 노드로 가는 최단거리
toX = dijk(x, brr, n)  # 각 노드에서 x로 가는 최단거리

max_t = 0
for i in range(1, n + 1):
    max_t = max(max_t, fromX[i] + toX[i])

print(max_t)