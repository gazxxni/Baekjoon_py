import sys
input = sys.stdin.readline

n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = list(range(n+1))
rank = [0] * (n+1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    else:
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
    return True

total = 0
max_edge = 0
cnt = 0

for w, u, v in edges:
    if unite(u, v):
        total += w
        if w > max_edge:
            max_edge = w
        cnt += 1
        if cnt == n-1:
            break

print(total - max_edge)
