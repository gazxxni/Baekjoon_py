board = input()

idx = 0
newboard = ''

while idx<len(board):
    if board[idx:idx+4]=='XXXX':
        newboard += 'AAAA'
        idx += 4
    elif board[idx:idx+2]=='XX':
        newboard +='BB'
        idx += 2
    elif board[idx]=='X':
        newboard = -1
        break
    else :
        newboard += board[idx]
        idx += 1

print(newboard)