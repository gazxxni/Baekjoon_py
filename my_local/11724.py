from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])  # 큐에 시작점을 넣고 시작
    visited[start] = True  # 시작점을 방문했다고 표시

    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft()  # 큐에서 노드를 하나 꺼냄
        for i in graph[v]: 
            if not visited[i]: 
                queue.append(i)
                visited[i] = True 

n, m = map(int, input().split()) 
graph = [[] for _ in range(n+1)] 

for i in range(m):
    u, v = map(int, input().split()) 
    graph[u].append(v)  # u에서 v 간선 추가
    graph[v].append(u)  # v에서 u 간선 추가 (무방향 그래프)

cnt = 0 
visited = [False] * (n+1)  # 각 노드의 방문 여부를 저장

for i in range(1, n+1): 
    if not visited[i]: 
        bfs(graph, i, visited) 
        cnt += 1  # BFS가 끝나면 하나의 연결 요소를 모두 방문, cnt 증가

print(cnt)
