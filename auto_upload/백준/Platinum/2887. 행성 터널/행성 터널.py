import sys
input = sys.stdin.readline

n = int(input())

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
xx, yy, zz = [], [], []
for i in range(n):
    x, y, z = map(int, input().split())
    xx.append((x, i))
    yy.append((y, i))
    zz.append((z, i))
    
xx.sort()
yy.sort()
zz.sort()

edge = []
for cur in xx, yy, zz:
    for i in range(1, n):
        w1, a = cur[i - 1]
        w2, b = cur[i]
        edge.append((abs(w1 - w2), a, b))
        
edge.sort()

parent = [i for i in range(n)]

def krustal():
    ans = 0
    
    for cost, a, b in edge:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            ans += cost
    
    return ans

print(krustal())