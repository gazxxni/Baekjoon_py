import sys
from collections import deque
input = sys.stdin.readline

q = deque()
n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
m = int(input())
crr = list(map(int, input().split()))

for i in range(n):
    if arr[i] == 0:
        q.append(brr[i])
        
ans = []
for i in range(m):
    q.appendleft(crr[i])
    ans.append(q.pop())
    
print(*ans)