r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
ans = 0
brr = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and not arr[nx][ny] in brr:
            brr.add(arr[nx][ny])
            dfs(nx, ny, cnt+1)
            brr.remove(arr[nx][ny])

brr.add(arr[0][0])
dfs(0, 0, 1)
print(ans)