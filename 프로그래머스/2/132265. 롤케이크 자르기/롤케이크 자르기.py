from collections import Counter
def solution(topping):
    answer = 0
    right = Counter(topping)
    left = set()
    
    r_cnt = len(right)
    l_cnt = 0
    for t in topping:
        if t not in left:
            left.add(t)
            l_cnt += 1
            
        right[t] -= 1
        if right[t] == 0:
            r_cnt -= 1
            
        if r_cnt == l_cnt:
            answer += 1
        
    return answer