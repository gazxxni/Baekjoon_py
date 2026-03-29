def solution(X, Y):
    dic_x = {i:0 for i in range(10)}
    dic_y = {i:0 for i in range(10)}
    answer = []
    
    for i in map(int, X):
        dic_x[i] += 1
    for i in map(int, Y):
        dic_y[i] += 1
    
    idx = 0
    for x, y in zip(dic_x.values(), dic_y.values()):
        if min(x, y) > 0:
            for _ in range(min(x, y)):
                answer.append(idx)
                
        idx += 1
        
    answer.sort(reverse=True)
    if answer:
        if sum(answer) == 0:
            return '0'
        else:
            return ''.join(map(str, answer))
    else:
        return '-1'