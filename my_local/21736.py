import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

# 상, 하, 좌, 우 방향을 나타내는 배열 (dx는 행 변화, dy는 열 변화)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부를 기록하는 배열
visited = [[0] * m for _ in range(n)]

# 캠퍼스 정보를 저장할 리스트
campus = []
Q = deque()

# 캠퍼스 맵 입력과 동시에 도연이의 위치 찾기
for i in range(n):
    campus.append(list(map(str, sys.stdin.readline().strip())))

    for j in range(len(campus[i])):
        if campus[i][j] == 'I':  # 도연이의 위치를 찾으면
            Q.append([i, j])  # 큐에 추가
            visited[i][j] = 1  # 방문 표시

answer = 0   # 도연이가 만난 사람 수

while Q:
    for _ in range(len(Q)):
        x, y = Q.popleft()  # 현재 좌표 (x, y)를 큐에서 꺼냄

        # 상, 하, 좌, 우 방향으로 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]  # 새로운 좌표 (nx, ny)

            # 캠퍼스 범위를 벗어나지 않고, 아직 방문하지 않았으며, 벽이 아닌 경우 이동
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and campus[nx][ny] != 'X':
                if campus[nx][ny] == 'P':  # 사람을 만났다면
                    answer += 1  # 만난 사람 수 증가

                visited[nx][ny] = 1  # 방문했다고 표시
                Q.append([nx, ny])  # 큐에 좌표 추가

if answer:  # 만난 사람이 있으면 그 수를 출력
    print(answer)
else:  # 만난 사람이 없으면 "TT" 출력
    print('TT')
