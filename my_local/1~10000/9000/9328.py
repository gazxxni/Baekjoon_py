import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(x, y, h, w, graph, key):
    visited = set()
    visited.add((x, y))
    q = deque()
    q.append((x, y))
    
    keys = set(key)
    cnt = 0
    waiting_doors = {}  # 열쇠 없는 문을 저장해두고 열쇠 발견시 다시 탐색

    while q:
        cx, cy = q.popleft()
        
        for xx, yy in direction:
            nx = cx + xx
            ny = cy + yy
            
            if 0 <= nx < w and 0 <= ny < h:
                if (nx, ny) not in visited:
                    word = graph[ny][nx]
                    
                    if word != '*':
                        if word == '.':
                            visited.add((nx, ny))
                            q.append((nx, ny))
                            
                        elif word.isupper():
                            if word.lower() in keys:
                                visited.add((nx, ny))
                                q.append((nx, ny))
                            else:
                                if word not in waiting_doors:
                                    waiting_doors[word] = []
                                waiting_doors[word].append((nx, ny))
                                
                        elif word.islower():
                            visited.add((nx, ny))
                            q.append((nx, ny))
                            if word not in keys:
                                keys.add(word)
                                door = word.upper()
                                if door in waiting_doors:
                                    for (door_x, door_y) in waiting_doors[door]:
                                        if (door_x, door_y) not in visited:
                                            visited.add((door_x, door_y))
                                            q.append((door_x, door_y))
                                    del waiting_doors[door]
                            
                        elif word == '$':
                            cnt += 1
                            visited.add((nx, ny))
                            q.append((nx, ny))
                            # 문서를 훔친 곳은 빈 공간으로 처리 (중복 카운트 방지)
                            graph[ny][nx] = '.' 
                            
    return cnt

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    
    # 맵 가장자리에 '.'을 추가하여 빌딩 밖에서 시작하는 로직을 단순화
    graph = [['.' for _ in range(w + 2)] for _ in range(h + 2)]
    for i in range(h):
        line = list(input().rstrip())
        for j in range(w):
            graph[i + 1][j + 1] = line[j]

    h += 2
    w += 2

    key = list(input().rstrip())

    ans = bfs(0, 0, h, w, graph, key)
        
    print(ans)