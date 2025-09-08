from collections import deque

m, n = map(int, input().split())

arr = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

q = deque()
# 토마토 익히기 위해 사용할 방향 배열 (상하좌우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 초기 익은 토마토의 위치를 큐에 추가합니다.
for i in range(n):  # 행
    for j in range(m):  # 열
        if arr[i][j] == 1:  # 익은 토마토인 경우
            q.append((i, j))  # 큐에 (행, 열) 추가

while q:
    x, y = q.popleft() 
    
    # 현재 토마토의 주변 4개 방향 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy 
        
        # 새로운 좌표가 배열의 범위 내에 있는지 체크
        if 0 <= nx < n and 0 <= ny < m:
            # 익지 않은 토마토인 경우
            if arr[nx][ny] == 0:  
                # 현재 토마토의 날짜 + 1로 익은 날짜를 설정
                arr[nx][ny] = arr[x][y] + 1  
                q.append((nx, ny))

# 결과 확인: 모든 토마토가 익었는지 확인
max_days = 0  # 최대 날짜를 저장할 변수
for i in range(n):  # 행
    for j in range(m):  # 열
        if arr[i][j] == 0:  # 익지 않은 토마토가 남아있는 경우
            print(-1)  # 모든 토마토가 익지 못했음을 출력
            exit(0)  
        max_days = max(max_days, arr[i][j])  # 최대 날짜 갱신

# 최종 결과 출력: 시작 상태를 제외하므로 1을 빼줍니다.
print(max_days - 1)  