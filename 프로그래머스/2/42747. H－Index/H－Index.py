def solution(citations):
    citations.sort(reverse=True)
    
    for i, cc in enumerate(citations):
        if cc < i + 1:
            return i
        
    return len(citations)