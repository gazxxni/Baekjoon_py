def solution(numbers):
    answer = set()
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if i != j:
                answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer