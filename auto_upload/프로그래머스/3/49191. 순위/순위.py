def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = -1
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                    
    cnt = 0
    for i in range(1, n+1):
        if graph[i][1:].count(1) + graph[i][1:].count(-1) == n - 1:
            cnt += 1
        
    return cnt