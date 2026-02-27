def solution(name):
    up_down = 0
    for char in name:
        up_down += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        
    n = len(name)
    move = n - 1
    
    for i in range(n):
        next_i = i + 1
        
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        move = min(move, i * 2 + n - next_i, i + 2 * (n - next_i))
        
    return up_down + move