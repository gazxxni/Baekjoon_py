from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    arr = [i for i in range(n)]
    per = list(permutations(arr, n))
    
    for p in per:
        cnt = 0
        num = k
        for i in range(len(p)):
            if num >= dungeons[p[i]][0]:
                num -= dungeons[p[i]][1]
                cnt += 1
                
            else:
                break
        
        answer = max(answer, cnt)

    
    return answer