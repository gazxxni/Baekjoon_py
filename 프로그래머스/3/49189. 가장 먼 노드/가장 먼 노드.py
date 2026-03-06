from collections import deque

def solution(n, edge):
    answer = 0
    
    def bfs(graph, start):
        distance = [-1] * (n+1)
        q = deque([start])
        distance[start] = 0
        
        while q:
            cur = q.popleft()
            
            for next in graph[cur]:
                if distance[next] == -1:
                    distance[next] = distance[cur] + 1
                    q.append(next)
        
        return distance
        
    graph = {i:[] for i in range(1, n+1)}
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    distances = bfs(graph, 1)
    return distances.count(max(distances))