from collections import deque

n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
q = deque(arr)
ans = []
idx = 0

while True:
    if not q:
        break
    
    if idx == k - 1:
        ans.append(q.popleft())
        idx = 0
        
    else:
        q.append(q.popleft())
        idx += 1
        
print("<" + ", ".join(map(str, ans)) + ">")
