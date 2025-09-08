import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)] 
distance = [INF] * (n+1)
brr = [0] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c)) 

st, ed = map(int, input().split())

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s)) 
    distance[s] = 0  

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                brr[i[0]] = now  
                heapq.heappush(q, (cost, i[0]))

dijkstra(st)
print(distance[ed])

ans = [ed]
a = ed
while a != st:
    a = brr[a]
    ans.append(a)

ans.reverse() 
print(len(ans))
print(*ans)