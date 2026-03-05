from collections import deque

def solution(n, edge):
    graph = {i : [] for i in range(1, n+1)}
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    def bfs(graph, start):
        distance = [-1] * (n+1)
        q = deque()
        q.append(start)
        distance[1] = 0

        while q:
            cur = q.popleft()
            
            for next in graph[cur]:
                if distance[next] == -1:
                    distance[next] = distance[cur] + 1
                    q.append(next)
        
        return distance
    
    distance = bfs(graph, 1)
    num = max(distance)
    cnt = 0
    for i in distance:
        if i == num:
            cnt += 1
    
    return cnt