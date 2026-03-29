def solution(n, words):
    answer = [words[0]]
    le = len(words)
    prev = answer[0][-1]
    num, turn = 0, 0
    for i in range(1, le):
        if words[i] in answer or prev != words[i][0]:
            num = i % n + 1
            turn = i // n + 1
            break
            
        answer.append(words[i])
        prev = words[i][-1]
        
    return [num, turn]