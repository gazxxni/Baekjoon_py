def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i
            
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    answer = answer.strip('.')
    
    if not answer:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
        
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer