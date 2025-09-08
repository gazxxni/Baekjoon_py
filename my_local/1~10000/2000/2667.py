from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

input_arr = [list(map(int, input().strip())) for _ in range(n)]

vilage_cnt = []  # 각 단지의 집 수를 저장할 리스트
visited = [[False] * n for _ in range(n)]
vilage = 0  # 단지 수

def BFS(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    cnt = 1   # 현재 단지에 속하는 집의 수

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):     # 상하좌우 탐색
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            # 배열을 벗어나지 않고, 집(1)이고 아직 방문하지 않은 곳이면 탐색
            if 0 <= nx < n and 0 <= ny < n and input_arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    return cnt

for i in range(n):
    for j in range(n):
        if input_arr[i][j] == 1 and not visited[i][j]:  # 집이 있고 방문하지 않은 경우
            vilage += 1    # 새로운 단지를 찾았으므로 단지 수 증가
            house_cnt = BFS(i, j)  # BFS로 단지 내 집의 수를 구함
            vilage_cnt.append(house_cnt)

vilage_cnt.sort()

print(vilage)

for cnt in vilage_cnt:
    print(cnt)

