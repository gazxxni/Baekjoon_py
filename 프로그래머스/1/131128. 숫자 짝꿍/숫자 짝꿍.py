from collections import defaultdict
def solution(X, Y):
    x = [int(i) for i in X]
    y = [int(i) for i in Y]
    dic_x = defaultdict(int)
    dic_y = defaultdict(int)
    for i in range(10):
        if i in x:
            dic_x[i] += x.count(i)
        else:
            dic_x[i] = 0
            
        if i in y:
            dic_y[i] += y.count(i)
        else:
            dic_y[i] = 0
            
    arr = []
    for x_i, x_v in dic_x.items():
        for y_i, y_v in dic_y.items():
            if x_i == y_i:
                cnt = max(x_v, y_v) - abs(x_v - y_v)
                for _ in range(cnt):
                    arr.append(x_i)
                break
                
    arr.sort(reverse=True)
    if arr:
        if sum(arr) == 0:
            return '0'
        else:
            return ''.join(map(str, arr))

    else:
        return '-1'