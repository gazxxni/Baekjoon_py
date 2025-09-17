from collections import deque

n, m = map(int, input().split())
arr = []
for i in  range(n):
    arr.append(list(input()))
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B': 
            bx, by = i, j
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    q = deque()
    q.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    cnt = 0
    result = -1
    
    while q:
        for _ in range(len(q)):
            rxx, ryy, bxx, byy = q.popleft()

            if cnt > 10:  # 횟수 초과
                return result
            
            if arr[rxx][ryy] == 'O':  # R이 구멍 만남
                return cnt
            
            for nx, ny in directions:
                nrx, nry = rxx, ryy
                
                while True:
                    nrx += nx
                    nry += ny
                    
                    if not (0 <= nrx < n and 0 <= nry < m):
                        break
                    
                    if arr[nrx][nry] == '#':  # 벽이면 하나 전으로
                        nrx -= nx
                        nry -= ny
                        break
                    
                    if arr[nrx][nry] == 'O':  # 구멍이면 탈출
                        break
                    
                nbx, nby = bxx, byy
                
                while True:
                    nbx += nx
                    nby += ny
                    
                    if not (0 <= nbx < n and 0 <= nby < m):
                        break
                    
                    if arr[nbx][nby] == '#':  # 벽이면 하나 전으로
                        nbx -= nx
                        nby -= ny
                        break
                    
                    if arr[nbx][nby] == 'O':  # 구멍이면 실패
                        break
                        
                if arr[nbx][nby] == 'O':  # 구멍이면 실패
                    continue
                
                if nrx == nbx and nry == nby:  # 둘이 같은 위치에 있으면
                    # R의 위치가 더 많이 움직이면 뒤에 있던 것
                    if abs(nrx - rxx) + abs(nry - ryy) > abs(nbx - bxx) + abs(nby - byy):
                        nrx -= nx
                        nry -= ny
                    else:
                        nbx -= nx
                        nby -= ny
                        
                if (nrx, nry, nbx, nby) not in visited:
                    q.append(((nrx, nry, nbx, nby)))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
        
    return result

ans = bfs()
print(ans)
    