from itertools import permutations 
def solution(n, weak, dist):
    len_weak = len(weak)
    for i in range(len_weak):
        weak.append(weak[i] + n)
        
    ans = len(dist) + 1
    
    for start in range(len_weak):
        for friend in list(permutations(dist, len(dist))):
            cnt = 1
            position = weak[start] + friend[cnt-1]
            
            for idx in range(start, start + len_weak):
                if position < weak[idx]:
                    cnt += 1
                    
                    if cnt > len(dist):
                        break
                        
                    position = weak[idx] + friend[cnt-1]
                    
            ans = min(ans, cnt)
        
    if ans > len(dist):
        return -1
    
    return ans