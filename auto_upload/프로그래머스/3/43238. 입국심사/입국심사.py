def solution(n, times):
    ans = 0
    st, ed = 1, n * max(times)
    
    while st <= ed:
        mid = (st + ed) // 2
        
        p = 0
        for t in times:
            p += mid // t
            
            if p >= n:
                break
                
        if p >= n:
            ans = mid
            ed = mid - 1
        else:
            st = mid + 1
    
    
    return ans