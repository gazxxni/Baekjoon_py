import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs():
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    contact = [[0] * m for _ in range(n)]

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif board[nx][ny] == 1:
                    contact[nx][ny] += 1

    melted = False
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and contact[i][j] >= 2:
                board[i][j] = 0
                melted = True

    return melted

def all_melted():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                return False
    return True

time = 0
while not all_melted():
    if bfs():
        time += 1

print(time)
