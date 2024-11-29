import sys

n, m = map(int, input().split())
arr = []

def dfs(x):
    if len(arr) == m:   # 종료 조건: arr의 길이가 m이면 현재 조합을 출력
        print(' '.join(map(str, arr)))
        return
    
    for i in range(x, n+1):   # x부터 n까지의 숫자를 순회하며 조합 생성
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()

dfs(1)

