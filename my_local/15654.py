import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
arr.sort()

def dfs(a):

    if a == m:  # 선택한 원소의 개수가 m개면 종료료
        print(' '.join(map(str, ans)))
        return

    for i in range(n):
        if arr[i] in ans:  # 중복 방지: 이미 선택된 숫자는 건너뛰기
            continue

        ans.append(arr[i])
        dfs(a + 1)
        ans.pop()

dfs(0)
