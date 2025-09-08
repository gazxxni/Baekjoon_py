import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

board = [list(map(int, list(input().rstrip()))) for _ in range(9)]
row = [[0]*10 for _ in range(9)]
col = [[0]*10 for _ in range(9)]
block = [[0]*10 for _ in range(9)]
empties = []

for r in range(9):
    for c in range(9):
        num = board[r][c]
        if num == 0:
            empties.append((r, c))
        else:
            row[r][num] = col[c][num] = block[(r//3)*3 + (c//3)][num] = 1

def dfs(idx):
    if idx == len(empties):
        for r in range(9):
            print(*board[r], sep='')
        sys.exit(0)
    r, c = empties[idx]
    b = (r//3)*3 + (c//3)
    for num in range(1, 10):
        if row[r][num] == 0 and col[c][num] == 0 and block[b][num] == 0:
            board[r][c] = num
            row[r][num] = col[c][num] = block[b][num] = 1
            dfs(idx + 1)
            board[r][c] = 0
            row[r][num] = col[c][num] = block[b][num] = 0

dfs(0)
