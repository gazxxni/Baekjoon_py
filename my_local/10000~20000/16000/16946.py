import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs_label(si, sj, cid, grid, comp_id, n, m):
    """
    (si, sj)에서 시작하는 0-영역을 BFS로 라벨링하고 그 크기를 반환한다.
    - grid: 0/1 맵 (list[list[int]])
    - comp_id: 각 칸의 컴포넌트 ID를 담는 2D 리스트 (-1: 미방문/벽)
    - cid: 이번에 부여할 컴포넌트 ID
    - n, m: 행/열 크기
    """
    q = deque()
    q.append((si, sj))
    comp_id[si][sj] = cid
    size = 1

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and comp_id[nx][ny] == -1:
                    comp_id[nx][ny] = cid
                    size += 1
                    q.append((nx, ny))
    return size

def label_components(grid, n, m):
    """
    모든 0-영역을 컴포넌트로 라벨링한다.
    반환:
      comp_id[i][j] = -1(미방문/벽) 또는 컴포넌트 ID(0..k-1)
      comp_size[cid] = 해당 컴포넌트의 크기
    """
    comp_id = [[-1] * m for _ in range(n)]
    comp_size = []
    cid = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and comp_id[i][j] == -1:
                size = bfs_label(i, j, cid, grid, comp_id, n, m)
                comp_size.append(size)
                cid += 1
    return comp_id, comp_size

def compute_answer(grid, comp_id, comp_size, n, m):
    """
    결과 맵을 문자열 리스트로 만든다.
    - 빈 칸(0): '0'
    - 벽(1): 인접한 서로 다른 컴포넌트 크기를 합쳐 1을 더하고 % 10
    """
    out_lines = []
    for i in range(n):
        row_chars = []
        for j in range(m):
            if grid[i][j] == 0:
                row_chars.append('0')
            else:
                seen = set()
                s = 1  # 현재 벽 칸을 부쉈을 때 생기는 칸 1개
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        ncid = comp_id[ni][nj]
                        if ncid != -1 and ncid not in seen:
                            seen.add(ncid)
                            s += comp_size[ncid]
                row_chars.append(str(s % 10))
        out_lines.append(''.join(row_chars))
    return out_lines


comp_id, comp_size = label_components(grid, n, m)
answer_lines = compute_answer(grid, comp_id, comp_size, n, m)
print('\n'.join(answer_lines))
