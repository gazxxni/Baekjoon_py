def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = [0]
    for i in range(1, n):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop(-1)
            answer[idx] = numbers[i]
        
        stack.append(i) 
            
    
            
    return answer