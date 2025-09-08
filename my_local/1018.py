import sys

n, m = map(int, input().split())

board = []  # 입력받은 보드
result = []  # 결과 값

for _ in range(n):
    board.append(input())

# 8x8 체스판을 만들기 위한 시작 좌표 (i, j)를 탐색
for i in range(n-7):  # 세로 범위
    for j in range(m-7):  # 가로 범위
        a1 = 0  # 'B'로 시작하는 체스판에서 칠해야 할 칸의 수
        a2 = 0  # 'W'로 시작하는 체스판에서 칠해야 할 칸의 수

        for a in range(i, i+8):
            for b in range(j, j+8):
               
                if (a+b) % 2 == 0:   # 좌표의 합이 짝수: 시작 칸과 같은 색이어야 함
                    if board[a][b] != 'B':  # 'B'로 시작하는 경우: 짝수 좌표에 'B'가 있어야 함
                        a1 += 1    # 다르면 칠해야 하므로 a1 증가
                    if board[a][b] != 'W':  # 'W'로 시작하는 경우: 짝수 좌표에 'W'가 있어야 함
                        a2 += 1    # 다르면 칠해야 하므로 a2 증가
                else:
                    # 좌표의 합이 홀수: 시작 칸과 반대 색이어야 함
                    if board[a][b] != 'W':  # 'B'로 시작하는 경우: 홀수 좌표에 'W'가 있어야 함
                        a1 += 1   # 다르면 칠해야 하므로 a1 증가
                    if board[a][b] != 'B':  # 'W'로 시작하는 경우: 홀수 좌표에 'B'가 있어야 함
                        a2 += 1  # 다르면 칠해야 하므로 a2 증가

        result.append(a1)
        result.append(a2)

print(min(result))
