n, m = map(int, input().split())
k = sorted(set(list(map(int, input().split()))))
ans = []
p = []

def dfs(depth, idx):
    if depth == m:
        print(*ans)
        return

    # idx부터 끝까지 탐색하면서 비내림차순을 유지
    for i in range(idx, len(k)):
        ans.append(k[i])  # 현재 숫자 선택
        dfs(depth+1, i)  # 같은 숫자를 중복 선택할 수 있으므로 `i`부터 다시 탐색
        ans.pop()   # 백트래킹(다음 경우를 위해 이전 선택을 되돌림)

dfs(0, 0)
p = sorted(list(set(p)))


