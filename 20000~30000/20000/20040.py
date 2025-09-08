import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]] 
        x = parent[x]
    return x

def union(a, b):
    root_a, root_b = find(a), find(b)
    if root_a == root_b:
        return False
    parent[root_b] = root_a
    return True

for i in range(1, m + 1):
    a, b = map(int, input().split())
    if not union(a, b):
        print(i)
        break
else:
    print(0)
 