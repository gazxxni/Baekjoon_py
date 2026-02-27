def solution(genres, plays):
    n = len(genres)
    arr = [(genres[i], plays[i], i) for i in range(n)]
    arr.sort(key=lambda x:(x[0], -x[1], x[2]))
    
    dic = {}
    for i in range(n):
        if genres[i] not in dic:
            dic[genres[i]] = plays[i]
        else:
            dic[genres[i]] += plays[i]
    
    dic = sorted(dic.items(), key=lambda x:-x[1])
    ans = []
    for i in dic:
        cnt = 0
        for j in arr:
            if i[0] == j[0]:
                cnt += 1
                
                if cnt > 2:
                    break
                else:
                    ans.append(j[2])
    
    return ans