def solution(routes):
    routes.sort(key=lambda x:x[1])
    camera = -99999999
    cnt = 0
    for route in routes:
        if route[0] > camera:
            camera = route[1]
            cnt +=1
    
    
    return cnt