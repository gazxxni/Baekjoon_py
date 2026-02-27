def solution(n, lost, reserve):
    new_lost = list(set(lost) - set(reserve))
    new_reserve = list(set(reserve) - set(lost))
    answer = n - len(new_lost)
    new_lost.sort()
    new_reserve.sort()
    
    arr = []
    for i in range(len(new_reserve)):
        for j in range(len(new_lost)):
            if new_reserve[i] + 1 == new_lost[j] or new_reserve[i] - 1 == new_lost[j]:
                if j not in arr:
                    arr.append(j)
                    break
    
    answer += len(arr)
    return answer