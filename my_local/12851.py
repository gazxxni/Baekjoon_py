import sys
from collections import deque

n, k = map(int, input().split())
arr = [-1] * 100001

def bfs(n, k):
    q = deque([n])
    arr[n] = 0
    cnt = 0

    while q:
        x = q.popleft()

        if x == k:
            cnt += 1  # 만날때마다 cnt 증가

        for i in (x-1, x+1, x*2):
            if 0 <= i < 100001:
                if arr[i] == -1 or arr[i] >= arr[x] + 1:
                    q.append(i)
                    arr[i] = arr[x] + 1

    return arr[k], cnt

a, b = bfs(n, k)
print(a)
print(b)
