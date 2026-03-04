from collections import deque

def solution(n, computers):
    visited = [False] * n
            
    def bfs(x):
        q = deque()
        q.append(x)
        visited[x] = True
        
        while q:
            cur = q.popleft()

            for next in range(n):
                if cur != next and computers[cur][next] == 1 and not visited[next]:
                    q.append(next)
                    visited[next] = True
    
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1
            
    return cnt