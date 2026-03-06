def check(answer):
    
    for x, y, item in answer:
        if item == 0:
            if y == 0 or (x, y-1, 0) in answer or (x-1, y, 1) in answer or (x, y, 1) in answer:
                continue
            return False
        
        elif item == 1:
            if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer or ((x-1, y, 1) in answer and (x+1, y, 1) in answer):
                continue
            return False
    
    return True


def solution(n, build_frame):
    answer = set()
    
    for x, y, item, build in build_frame:
        thing = (x, y, item)
        
        if build == 1:
            answer.add(thing)
            if not check(answer):
                answer.remove(thing)
                
        elif build == 0:
            answer.remove(thing)
            if not check(answer):
                answer.add(thing)
    
    
    return sorted(list(answer))