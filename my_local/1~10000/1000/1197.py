import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))  

parent = [i for i in range(v + 1)]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]] 
        x = parent[x]
    return x

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root
        return True
    return False

edges.sort()

total = 0
for cost, a, b in edges:
    if union(a, b):
        total += cost

print(total)
