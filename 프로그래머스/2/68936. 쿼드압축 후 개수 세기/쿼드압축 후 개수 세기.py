def solution(arr):
    answer = [0, 0]
    def recursive(x, y, length):
        num = arr[x][y]
        for i in range(x, x+length):
            for j in range(y, y+length):
                if num != arr[i][j]:
                    num = arr[i][j]
                    recursive(x, y, length//2)
                    recursive(x+length//2, y, length//2)
                    recursive(x, y+length//2, length//2)
                    recursive(x+length//2, y+length//2, length//2)
                    return
            
        if num == arr[x][y]:
            answer[num] += 1
                
        return answer
    
    aa = recursive(0, 0, len(arr))
    
    return answer