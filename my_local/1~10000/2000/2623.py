import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * 10001

for _ in range(m):
    data = list(map(int, input().split()))
    order = data[1:] 

    for i in range(len(order) - 1):
        a, b = order[i], order[i + 1]
        graph[a].append(b)
        indegree[b] += 1



def topological_sort():
    q = deque()

    for i in range(1, n + 1): 
        if indegree[i] == 0:
            q.append(i)

    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return result

ans = topological_sort()

if len(ans) == n:
    for x in ans:
        print(x)
else:
    print(0)

