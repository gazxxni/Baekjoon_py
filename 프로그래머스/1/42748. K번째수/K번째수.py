def solution(array, commands):
    answer = []
    
    for row in commands:
        arr = array[row[0] - 1:row[1]]
        arr.sort()
        answer.append(arr[row[2] - 1])
        
    return answer