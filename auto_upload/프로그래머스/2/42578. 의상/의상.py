def solution(clothes):
    answer = 1
    dic = {}
    
    for k, v in clothes:
        if v in dic:
            dic[v] += 1
        else:
            dic[v] = 1
    
    for k, v in dic.items():
        answer *= (v + 1)
        
    return answer - 1