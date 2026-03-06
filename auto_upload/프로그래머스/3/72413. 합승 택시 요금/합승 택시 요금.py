import heapq

def solution(n, s, a, b, fares):
    answer = 0
    
    graph = {i:{} for i in range(1, n+1)}
    for u, v, w in fares:
        graph[u][v] = w
        graph[v][u] = w
        
    def dijk(graph, start):
        distance = {i:float('inf') for i in range(1, n+1)}
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
    
    dist_s = dijk(graph, s)
    dist_a = dijk(graph, a)
    dist_b = dijk(graph, b)
    
    min_fare = float('inf')
    
    for i in range(1, n+1):
        cur_fare = dist_s[i] + dist_a[i] + dist_b[i]
        min_fare = cur_fare if cur_fare < min_fare else min_fare
        
    return min_fare