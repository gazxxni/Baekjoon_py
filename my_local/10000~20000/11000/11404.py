# 다익스트라

import heapq

n = int(input())
m = int(input())
INF = 1e8

graph = [[] for _ in range(n+1)] 

distance = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split()) 
    graph[u].append((v, w))  

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start][start] = 0  

    while q:
        dist, now = heapq.heappop(q)

        if distance[start][now] < dist:
            continue

        for i in graph[now]:  
            cost = dist + i[1]
            if cost < distance[start][i[0]]:  
                distance[start][i[0]] = cost  
                heapq.heappush(q, (cost, i[0]))

for i in range(1, n+1): 
    dijkstra(i)

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == INF:
            print(0, end=" ")
        else:
            print(distance[i][j], end=" ")
    print()



# ------------------------------------------------------------------
# 플로이드 와샬

# import sys
# INF = int(1e9)

# n = int(sys.stdin.readline())  # 도시의 수
# m = int(sys.stdin.readline())  # 버스의 수

# graph = [[INF] * (n + 1) for _ in range(n + 1)]    # 모든 최단 거리를 저장
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             graph[i][j] = 0

# for _ in range(m):
#     a, b, c = map(int, sys.stdin.readline().split())
#     graph[a][b] = min(c, graph[a][b])   # 노선이 하나가 아닐 수 있음 > 최소값 넣기 

# # 2. 다이나믹 프로그래밍
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if graph[a][b] == INF:
#             print("0",  end=" ")
#         else:
#             print(graph[a][b], end=" ")
#     print()