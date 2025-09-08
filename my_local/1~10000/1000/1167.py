from collections import deque

v = int(input())
arr = [[] for _ in range(v+1)]

for i in range(v):
    a = list(map(int, input().split()))
    for j in range(1, len(a)-1, 2):
        arr[a[0]].append((a[j], a[j+1]))
    for j in range(1, len(a)-1, 2):
        arr[a[j]].append((a[0], a[j+1]))

def bfs(s):
    q = deque()
    q.append((s, 0))
    visited = [0] * (v+1)
    visited[s] = 1
    max_dist = 0
    max_node = s

    while q:
        node, dist = q.popleft()

        for i in arr[node]:
            if not visited[i[0]]:
                visited[i[0]] = 1
                q.append((i[0], dist + i[1]))
                if dist + i[1] > max_dist:
                    max_dist = dist + i[1]
                    max_node = i[0]

    return max_node, max_dist

a, b = bfs(1)
c, d = bfs(a)
print(d)