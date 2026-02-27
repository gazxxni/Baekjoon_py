def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [(0, prices[0])]
    
    for i, v in enumerate(prices[1:n], start=1):
        while stack and stack[-1][1] > v:
            answer[stack[-1][0]] = i - stack[-1][0]
            stack.pop(-1)
        stack.append((i, v))
        
    while stack:
        answer[stack[-1][0]] = (n - 1) - stack[-1][0]
        stack.pop(-1)
        
    return answer