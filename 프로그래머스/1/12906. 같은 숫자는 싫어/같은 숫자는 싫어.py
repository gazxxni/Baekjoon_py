def solution(arr):
    answer = [arr[0]]
    n = len(arr)
    for i in range(1, n):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer