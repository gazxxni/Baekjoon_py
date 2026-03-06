def is_possible(stones, k, mid):
    skip = 0
    
    for stone in stones:
        if stone < mid:
            skip += 1
            
            if skip >= k:
                return False
            
        else:
            skip = 0
            
    return True

def solution(stones, k):
    st, ed = 1, max(stones)
    
    people = 0
    while st <= ed:
        mid = (st + ed) // 2
        
        if is_possible(stones, k, mid):
            people = mid
            st = mid + 1
        else:
            ed = mid - 1
        
        
        
    return people