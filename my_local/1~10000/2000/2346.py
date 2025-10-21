from collections import deque

n = int(input())
arr = list(map(int, input().split()))
q = deque()
a = 0
for i in arr:
    q.append((a, i))
    a += 1

ans = []
while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(*ans)