from collections import deque

def solution(n, wires):
    answer = float('inf')
    graph = {i:[] for i in range(1, n+1)}
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start):
        q = deque([start])
        visited = {start}
        cnt = 0
        while q:
            cur = q.popleft()
            cnt += 1
            for next in graph[cur]:
                if next not in visited:
                    visited.add(next)
                    q.append(next)
                    
        return cnt
    
    for u, v in wires:
        graph[u].remove(v)
        graph[v].remove(u)

        cnt1 = bfs(u)
        cnt2 = n - cnt1
        answer = min(answer, abs(cnt1 - cnt2))

        graph[u].append(v)
        graph[v].append(u)
            
    return answer