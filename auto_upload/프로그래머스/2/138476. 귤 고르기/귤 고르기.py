from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)

    for v in sorted(cnt.values(), reverse=True):
        if k <= 0:
            break
        
        k -= v  
        answer += 1 
        
    return answer