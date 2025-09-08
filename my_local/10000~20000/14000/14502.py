import sys
import copy
from collections import deque
input= sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def virus():
    tmp = copy.deepcopy(arr)  
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2 
                q.append((nx, ny))

    global cnt
    safe = sum(row.count(0) for row in tmp)
    cnt = max(cnt, safe)

def build_walls(count):
    if count == 3:  
        virus()
        return
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0: 
                arr[i][j] = 1 
                build_walls(count + 1)  
                arr[i][j] = 0  

build_walls(0)
print(cnt)
