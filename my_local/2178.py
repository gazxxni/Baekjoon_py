from collections import deque

n, m = map(int, input().split())
graph = [] 

for _ in range(n):  # rstrip()로 '\n' 제거 후, 한 줄을 리스트로 변환하여 추가
    graph.append(list(map(int, input().rstrip())))  

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 


def bfs(x, y):
    
    queue = deque()  
    queue.append((x, y))  

    while queue:
        x, y = queue.popleft() 

        for i in range(4):
            nx = x + dx[i]  
            ny = y + dy[i] 

            # 이동한 좌표가 미로 범위 안에 있고, 아직 방문하지 않은 길(1)인 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))  # 이동할 좌표를 큐에 추가
                graph[nx][ny] = graph[x][y] + 1  # 이전 좌표까지의 이동 거리 +1
    
    # 도착 지점의 값(최단 경로 거리)을 반환
    return graph[n-1][m-1]

print(bfs(0,0))
