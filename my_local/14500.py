import sys

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1]  

max_a = 0  # 최대값을 저장할 변수

def dfs(x, y, tmp, cnt):
    global max_a

    if cnt == 4:  # 테트로미노 4칸을 모두 선택했으면 최대값 갱신
        max_a = max(max_a, tmp)
        return
    
    for i in range(4):
        nx = x + dx[i]  
        ny = y + dy[i]  

        # 경계 조건과 방문 여부 체크
        if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
            continue
        
        # 다음 좌표 방문 처리 및 DFS 호출
        visited[ny][nx] = True
        dfs(nx, ny, tmp + graph[ny][nx], cnt + 1)
        visited[ny][nx] = False  # DFS 종료 후 방문 해제 (백트래킹)


# 'ㅗ' 모양 처리 함수
def fy(x, y):
    global max_a
    tmp = graph[y][x]  # 현재 위치의 값
    arr = []  # 주변 4개의 값 저장

    for i in range(4):
        nx = x + dx[i]  
        ny = y + dy[i]  

        # 경계 조건 체크
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        arr.append(graph[ny][nx])  # 유효한 값만 추가

    length = len(arr)

    # 주변 값이 4개일 경우, 가장 작은 값을 제외하고 계산
    if length == 4:
        arr.sort(reverse=True)  # 내림차순 정렬
        arr.pop()               # 가장 작은 값 제거
        max_a = max(max_a, sum(arr) + graph[y][x])

    # 주변 값이 3개일 경우, 그대로 계산
    elif length == 3:
        max_a = max(max_a, sum(arr) + graph[y][x])
    return

for i in range(n):
    for j in range(m):
        # DFS로 테트로미노 4칸 합 계산
        visited[i][j] = True
        dfs(j, i, graph[i][j], 1)
        visited[i][j] = False
        fy(j, i)

print(max_a)
