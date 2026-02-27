from collections import Counter

def solution(n, stages):
    answer = [0] * (n + 2)
    people = len(stages)
    stages.sort()
    
    cnt = Counter(stages)
    
    for k, v in cnt.items():
        answer[k] = v / people
        people -= v
    
    
    answer.pop(-1)
    ans = []
    for i, v in enumerate(answer[1:n+1], start=1):
        ans.append((i, v))
    
    ans.sort(key=lambda x:x[1], reverse=True)
    
    ans = [ans[i][0] for i in range(len(ans))]
    return ans