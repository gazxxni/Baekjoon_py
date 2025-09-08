n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(start):
    stack = [(start, 0)]
    visited = [False] * (n+1)
    visited[start] = True
    max_node, max_dist = start, 0

    while stack:
        node, dist = stack.pop()
        if dist > max_dist:
            max_node, max_dist = node, dist

        for next_node, next_dist in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node, dist + next_dist))

    return max_node, max_dist

node1, _ = dfs(1)  # 1번 노드와 가장 멀리 떨어진 노드 찾기
_, answer = dfs(node1)  # 위에서 찾은 노드와 가장 멀리 떨어진 노드 찾기
print(answer)