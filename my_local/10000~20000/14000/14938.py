import heapq

n, m, r = map(int, input().split())
arr = list(map(int, input().split()))
INF = int(1e8)

graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, i = map(int, input().split()) 
    graph[a].append((b, i)) 
    graph[b].append((a, i))  

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0  

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:  
            cost = dist + i[1]
            if cost < distance[i[0]]:  
                distance[i[0]] = cost  
                heapq.heappush(q, (cost, i[0]))
    
    return distance

max_items = 0
for i in range(1, n+1): 
    dist = dijkstra(i)
    total_items = 0 

    for j in range(1, n + 1):
        if dist[j] <= m: 
            total_items += arr[j - 1] 

    max_items = max(max_items, total_items)

print(max_items)
