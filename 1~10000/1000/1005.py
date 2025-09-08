import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    drr = list(map(int, input().split()))
    
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    dp = [0] * n
    
    for _ in range(k):
        x, y = map(int, input().split())    
        graph[x-1].append(y-1)
        indegree[y-1] += 1
        
    w = int(input())
    
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = drr[i]
            
    while q:
        cur = q.popleft()
        
        for next in graph[cur]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[cur] + drr[next])
            
            if indegree[next] == 0:
                q.append(next)
                
    print(dp[w-1])