from collections import deque

n = int(input())
grapgh = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]    # BFS 중복 방문 방지를 위한 check 배열

    while queue:
        q = queue.popleft()

        for i in range(n):
            # 아직 방문하지 않았고, q에서 i로 가는 길이 있을 때
            if check[i] == 0 and grapgh[q][i] == 1:
                queue.append(i)      # 큐에 i 노드를 추가하고 방문 기록
                check[i] = 1
                # 노드 x에서 노드 i로 가는 경로가 있음을 visited 배열에 기록
                visited[x][i] = 1

for i in range(n):
    bfs(i)

for i in visited:
    print(*i)
