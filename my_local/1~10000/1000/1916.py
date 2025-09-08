import sys
import heapq

INF = int(1e9)   # 무한대를 나타내는 값

n = int(input()) 
m = int(input()) 
graph = [[] for _ in range(n + 1)] 
costs = [INF] * (n + 1)  # 최소 비용 테이블 초기화

for _ in range(m):
    u, v, w = map(int, input().split())  # u: 시작 도시, v: 도착 도시, w: 비용
    graph[u].append((v, w))  # u -> v, 비용 w

a, b = map(int, input().split())

def search(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작 노드 (비용 0, 시작점)
    costs[start] = 0  # 시작 노드의 최소 비용 0

    while q:
        current_cost, now = heapq.heappop(q)  # 현재 최소 비용이 가장 작은 노드를 꺼냄

        if costs[now] < current_cost:   # 이미 처리된 적이 있는 노드는 무시
            continue

        for next_node, weight in graph[now]:  # 현재 노드와 연결된 인접 노드 확인
            cost = current_cost + weight

            # 현재 노드를 통해 다른 노드로 가는 비용이 더 적다면 갱신
            if cost < costs[next_node]:
                costs[next_node] = cost
                heapq.heappush(q, (cost, next_node))  # 갱신된 비용을 큐에 추가

search(a)
print(costs[b]) 
