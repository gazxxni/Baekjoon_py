import sys
from collections import deque

s = sys.stdin.readline().rstrip()
q = deque()
ans = []
flag = False

for word in s:
    if word == '<':
        flag = True
        while q:
            ans.append(q.popleft())
        ans.append(word)
    
    elif word == '>':
        flag = False
        ans.append(word)
    
    elif flag:
        ans.append(word)
        
    elif word == ' ':
        while q:
            ans.append(q.popleft())
        ans.append(word)
        
    else:
        q.appendleft(word)

while q:
    ans.append(q.popleft())

print(''.join(ans))