def solution(n, left, right):
    ans = []
    for k in range(left, right + 1):
        i = k // n
        j = k % n
        
        ans.append(max(i, j) + 1)
    
    return ans