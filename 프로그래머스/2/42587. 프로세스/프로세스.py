from collections import deque

def solution(priorities, location):
    q = deque([(v, i) for i, v in enumerate(priorities)])
    cnt = 1
    
    while q:
        cv, ci = q.popleft()
        
        if q and cv < max(q)[0]:
            q.append((cv, ci))
            
        else:
            if ci == location:
                break
            else:
                cnt += 1
                
    return cnt