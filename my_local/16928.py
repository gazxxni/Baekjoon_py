from collections import deque 

n, m = map(int, input().split())

board = [0] * 101  # 최소 주사위 횟수를 기록
visited = [False] * 101 

a = dict()  # 사다리 정보 저장
for _ in range(n):
    x, y = map(int, input().split())
    a[x] = y 

b = dict()  # 뱀 정보 저장
for _ in range(m):
    u, v = map(int, input().split())
    b[u] = v 


def bfs(s):
    q = deque() 
    q.append(s) 
    visited[s] = True 

    while q: 
        t = q.popleft()  
        
        for i in range(1, 7):  # 주사위로 1부터 6까지 이동
            next = t + i  # 다음 위치 계산
            
            # 다음 위치가 게임판 범위 안이고 방문하지 않은 경우
            if 0 < next <= 100 and not visited[next]:
                
                if next in a:  # 사다리가 있으면 올라감
                    next = a[next]

                
                if next in b:  # 뱀이 있으면 내려감
                    next = b[next]

                # 최종 위치를 아직 방문하지 않았다면 큐에 추가
                if not visited[next]:
                    q.append(next)
                    visited[next] = True 
                    board[next] = board[t] + 1  # 최소 주사위 횟수 기록

bfs(1)
print(board[100])
