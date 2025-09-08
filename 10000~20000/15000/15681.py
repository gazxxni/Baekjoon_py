import sys
input = sys.stdin.readline

n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0] * (n+1)
parent[r] = r
order = []
stack = [r]
while stack:
    u = stack.pop()
    order.append(u)
    for v in graph[u]:
        if parent[v] == 0:
            parent[v] = u
            stack.append(v)

subtree_size = [0] * (n+1)
for u in reversed(order):
    sz = 1
    for v in graph[u]:
        if parent[v] == u:
            sz += subtree_size[v]
    subtree_size[u] = sz

for _ in range(q):
    u = int(input())
    print(subtree_size[u])