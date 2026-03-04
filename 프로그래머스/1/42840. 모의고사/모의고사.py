def solution(answers):
    ans = []
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    dic = {1: 0, 2: 0, 3: 0}
    
    for i in range(len(answers)):
        idx_1 = i % len(one)
        idx_2 = i % len(two)
        idx_3 = i % len(three) 
        
        if answers[i] == one[idx_1]:
            dic[1] += 1
        if answers[i] == two[idx_2]:
            dic[2] += 1
        if answers[i] == three[idx_3]:
            dic[3] += 1
            
    max_num = max(dic.values())
    
    for k, v in dic.items():
        if v == max_num:
            ans.append(k)
    
    return ans