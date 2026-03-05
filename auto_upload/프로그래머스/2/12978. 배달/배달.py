import heapq
def solution(N, road, K):
    
    def dijk(graph, start):
        distance = {i: float('inf') for i in range(1, N+1)}
        distance[start] = 0
        q = [(0, start)]
        
        while q:
            cur_dist, cur_node = heapq.heappop(q)
            
            if distance[cur_node] < cur_dist:                    
                continue
                
            for adj, weight in graph[cur_node].items():
                dist = cur_dist + weight
                
                if dist < distance[adj]:
                    distance[adj] = dist
                    heapq.heappush(q, (dist, adj))
            
        return distance
    
    graph = {i: {} for i in range(1, N+1)}
    for u, v, w in road:
        if v in graph[u]:
            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(graph[v][u], w)
        else:
            graph[u][v] = w
            graph[v][u] = w
    
    distance = dijk(graph, 1)
    
    cnt = 0
    for v in distance.values():
        if v <= K:
            cnt += 1

    return cnt