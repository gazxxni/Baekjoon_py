import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())

def bfs(a, b):
    q = deque()
    q.append((a, 1))  # (현재 숫자, 변환 횟수)

    while q:
        now, cnt = q.popleft()

        if now > b:
            continue

        if now == b:
            return cnt  

        q.append((now * 2, cnt + 1))
        q.append((int(str(now) + "1"), cnt + 1))

    return -1  

print(bfs(a, b))
