import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

white_cells = []
black_cells = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            # (행 + 열)이 짝수이면 '흰색' 칸으로 간주
            if (r + c) % 2 == 0:
                white_cells.append((r, c))
            else:
                black_cells.append((r, c))

# 대각선 방문 여부를 체크
# (r-c) 대각선 (인덱스: r - c + n - 1 사용)
diag1 = [False] * (2 * n - 1)
# (r+c) 대각선 (인덱스: r + c 사용)
diag2 = [False] * (2 * n - 1)

def solve(cell_list, index):
    # 리스트의 모든 칸을 다 확인했다면 0 반환
    if index == len(cell_list):
        return 0

    # 현재 확인할 칸의 좌표
    r, c = cell_list[index]

    # 현재 칸(r, c)에 비숍을 놓지 않는 경우
    # 이 칸을 건너뛰고, 다음 칸(index + 1)부터 탐색
    res = solve(cell_list, index + 1)

    # 현재 칸(r, c)에 비숍을 놓는 경우
    diag1_idx = r - c + n - 1
    diag2_idx = r + c

    # 두 대각선이 비었는지 확인
    if not diag1[diag1_idx] and not diag2[diag2_idx]:
        diag1[diag1_idx] = True
        diag2[diag2_idx] = True

        # 현재 칸에 1개를 놓았으니, 1 + 다음 칸(index+1)부터 탐색
        placed_count = 1 + solve(cell_list, index + 1)

        # 사용 후 두 대각선 사용 해제
        diag1[diag1_idx] = False
        diag2[diag2_idx] = False
        
        # 놓지 않은 경우(res)와 놓은 경우(placed_count) 중 더 큰 값으로 res를 갱신
        res = max(res, placed_count)

    return res

# 흰색 칸들에 대해 백트래킹 실행
ans_white = solve(white_cells, 0)

# 검은색 칸들에 대해 백트래킹 실행
# 검은색 칸 탐색을 위해 대각선 배열(diag1, diag2)을 다시 초기화
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)
ans_black = solve(black_cells, 0)

print(ans_white + ans_black)