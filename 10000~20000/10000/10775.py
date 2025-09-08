import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
arr = [int(input()) for _ in range(p)]
parent = [i for i in range(g + 1)]

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    rootA = find(a, parent)
    rootB = find(b, parent)
    
    parent[rootA] = rootB

cnt = 0
for i in arr:
    gate = find(i, parent)
    
    if gate == 0:
        break
    else:
        cnt += 1
        union(gate, gate - 1, parent)
        
print(cnt)