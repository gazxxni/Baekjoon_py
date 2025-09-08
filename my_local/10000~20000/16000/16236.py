import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark_x, shark_y = i, j
            board[i][j] = 0 

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

size = 2
eat = 0
time = 0

def bfs(x, y, size):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    fish = []

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    # 상어가 이동할 수 있는 경우
                    if board[nx][ny] <= size:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                        # 먹을 수 있는 물고기면 후보 등록
                        if 0 < board[nx][ny] < size:
                            fish.append((visited[nx][ny], nx, ny))

    # 가장 가까운 물고기 선택
    if not fish:
        return None
    fish.sort()  # 거리, x, y 순으로 정렬
    return fish[0]  # (거리, x, y)

while True:
    result = bfs(shark_x, shark_y, size)

    if result is None:  # 더 이상 먹을 물고기 없음
        break

    dist, nx, ny = result

    # 상어 이동
    shark_x, shark_y = nx, ny
    time += dist

    # 물고기 먹기
    board[nx][ny] = 0
    eat += 1

    # 크기 증가
    if eat == size:
        size += 1
        eat = 0

print(time)
