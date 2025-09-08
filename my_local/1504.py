import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    x, y, c = map(int, input().split())
    graph[x].append((y, c))
    graph[y].append((x, c))

def dijk(st):
    q = []
    dist = [INF] * (v+1)
    heapq.heappush(q, (0, st))
    dist[st] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue

        for i in graph[now]:
            cost = d + i[1]

            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        
    return dist

v1, v2 = map(int, input().split())

a = dijk(1)  # 1번 노드에서 시작하는 최단 거리 배열
v1_dist = dijk(v1)  # v1번 노드에서 시작하는 최단 거리 배열
v2_dist = dijk(v2)  # v2번 노드에서 시작하는 최단 거리 배열

path1 = a[v1] + v1_dist[v2] + v2_dist[v]  # 경로 1: 1 → v1 → v2 → v (v번 정점까지)
path2 = a[v2] + v2_dist[v1] + v1_dist[v]  # 경로 2: 1 → v2 → v1 → v (v번 정점까지)

result = min(path1, path2)
print(result if result < INF else -1)