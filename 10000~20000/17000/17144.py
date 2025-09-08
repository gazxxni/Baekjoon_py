import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

def diffuse():
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    amount = [[board[i][j] // 5 for j in range(c)] for i in range(r)]
    updated = [[0] * c for _ in range(r)]

    filter = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == -1:
                filter.append(i)
                updated[i][j] = -1
                continue

            count = 4
            added = 0
            for d in directions:
                x, y = i + d[0], j + d[1]

                if x < 0 or x >= r or y < 0 or y >= c or board[x][y] == -1:
                    count -= 1
                else:
                    added += amount[x][y]

            updated[i][j] = board[i][j] - (amount[i][j] * count) + added

    return filter[0], filter[1], updated

def activate(f_x, f_y):

    for row in range(f_x - 1, 0, -1):
        board[row][0] = board[row - 1][0]
    for col in range(c - 1):
        board[0][col] = board[0][col + 1]
    for row in range(f_x):
        board[row][-1] = board[row + 1][-1]
    for col in range(c - 1, 0, -1):
        board[f_x][col] = board[f_x][col - 1]
    board[f_x][1] = 0

    for row in range(f_y + 1, r - 1):
        board[row][0] = board[row + 1][0]
    for col in range(c - 1):
        board[-1][col] = board[-1][col + 1]
    for row in range(r - 1, f_y, -1):
        board[row][-1] = board[row - 1][-1]
    for col in range(c - 1, 0, -1):
        board[f_y][col] = board[f_y][col - 1]
    board[f_y][1] = 0

def sum_dust():
    result = 0
    for row in board:
        result += sum(row)
    return result + 2 

for _ in range(t):
    x, y, board = diffuse()
    activate(x, y)

print(sum_dust())
