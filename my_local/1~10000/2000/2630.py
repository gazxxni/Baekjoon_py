import sys
input=sys.stdin.readline

white = 0
blue = 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def divide(x, y, size):
    global white, blue

    # 첫 번째 칸의 색상을 기준으로 설정
    color = arr[x][y]

    # 해당 영역의 모든 칸이 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != color:
                # 색상이 다른 경우 4등분하여 재귀적으로 처리
                half = size // 2
                divide(x, y, half)  # 왼쪽 위
                divide(x, y + half, half)  # 오른쪽 위
                divide(x + half, y, half)  # 왼쪽 아래
                divide(x + half, y + half, half)  # 오른쪽 아래
                return

    # 모두 같은 색이라면 해당 색의 카운트를 증가시킴
    if color == 0:
        white += 1
    else:
        blue += 1

# 전체 색종이를 나누는 재귀 함수 호출
divide(0, 0, n)

# 결과 출력
print(white)
print(blue)

