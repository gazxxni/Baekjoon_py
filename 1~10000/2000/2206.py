from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1  

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))  # (x좌표, y좌표, 벽을 부쉈는지 여부)

    while queue:
        x, y, w = queue.popleft()

        # 목표 지점에 도달한 경우
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        # 상하좌우 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 맵 범위 안에 있는지 확인
            if 0 <= nx < n and 0 <= ny < m:
                # 다음 이동할 곳이 벽이고, 벽을 부수지 않은 상태라면
                if grid[nx][ny] == 1 and w == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))

                # 다음 이동할 곳이 벽이 아니고 아직 방문하지 않은 경우
                if grid[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append((nx, ny, w))

    return -1  # 목표 지점에 도달하지 못한 경우

print(bfs())