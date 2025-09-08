from collections import deque

def BFS(x, y):
    q.append((x, y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i] 
            ny = y + dy[i] 

            # 경계 안에 있고, 현재 색과 동일하며, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문 처리
                q.append((nx, ny))  # 큐에 추가

n = int(input())
a = [list(input()) for _ in range(n)]
q = deque()

visited = [[0] * n for _ in range(n)]
cnt_1 = 0  # 정상 시각 그룹의 개수


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            cnt_1 += 1 

# 적록색약 처리를 위해 'G'를 'R'로 변경
for i in range(n):
    for j in range(n):
        if a[i][j] == 'G':
            a[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
cnt_2 = 0  # 적록색약 그룹의 개수

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            cnt_2 += 1  # 적록색약 그룹 카운트 증가

print(cnt_1, cnt_2)
