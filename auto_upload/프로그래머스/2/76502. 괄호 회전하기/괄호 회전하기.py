def solution(s):
    answer = 0
    new = s * 2
    n = len(s)
    for i in range(n):
        stack = [new[i]]
        for word in new[i+1:i+n]:
            if stack:
                if stack[-1] == '(' and word == ')':
                    stack.pop(-1)
                elif stack[-1] == '[' and word == ']':
                    stack.pop(-1)
                elif stack[-1] == '{' and word == '}':
                    stack.pop(-1)
                else:
                    stack.append(word)
                    
            else:
                if word in ('{', '[', '('):
                    stack.append(word)
                
            
        
        if not stack:
            answer += 1
            
    
        
    return answer