def solution(citations):
    citations.sort(reverse=True)
    for i, v in enumerate(citations):
        if v < i + 1:
            return i
    return len(citations)