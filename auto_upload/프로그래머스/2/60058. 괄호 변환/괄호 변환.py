def solution(p):
    if not p:
        return ""

    u = ""
    v = ""
    left_count = 0 
    right_count = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            left_count += 1
        else:
            right_count += 1
            
        if left_count == right_count:
            u = p[:i+1]
            v = p[i+1:]
            break

    is_correct = True
    stack = []
    
    for char in u:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                is_correct = False
                break
            stack.pop()
            
    if is_correct:
        return u + solution(v)
        
    else:
        answer = ""
        answer += "("
        answer += solution(v)
        answer += ")"

        for char in u[1:-1]:
            if char == '(':
                answer += ')'
            else:
                answer += '('

        return answer