def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if 0 < j < len(triangle[i-1]):
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]
            else:
                triangle[i][j] += triangle[i-1][j-1]
    
    return max(triangle[len(triangle) - 1])