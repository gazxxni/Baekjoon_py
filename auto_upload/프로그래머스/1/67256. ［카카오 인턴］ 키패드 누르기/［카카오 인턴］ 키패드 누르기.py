def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']]
    dic = {}
    for i in range(4):
        for j in range(3):
            dic[keypad[i][j]] = (i, j)
            
    left = [1, 4, 7]
    right = [3, 6, 9]
    cur_left = '*'
    cur_right = '#'
    
    for i in numbers:
        if i in left:
            answer += 'L'
            cur_left = i
            
        elif i in right:
            answer += 'R'
            cur_right = i
            
        else:
            r_x, r_y = dic[cur_right]
            l_x, l_y = dic[cur_left]
            c_x, c_y = dic[i]
            
            if (abs(c_x - r_x) + abs(c_y - r_y)) > (abs(c_x - l_x) + abs(c_y - l_y)):
                answer += 'L'
                cur_left = i
            
            elif (abs(c_x - r_x) + abs(c_y - r_y)) < (abs(c_x - l_x) + abs(c_y - l_y)):
                answer += 'R'
                cur_right = i
            else:
                if hand == 'right':
                    answer += 'R'
                    cur_right = i
                else:
                    answer += 'L'
                    cur_left = i
        
        
    return answer