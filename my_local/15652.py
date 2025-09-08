import sys

n, m = map(int, input().split())
arr = []

def dfs(a):
    if len(arr) == m:  # m개의 숫자가 들어갔을 때 재귀 종료
        print(' '.join(map(str, arr)))  # 리스트를 문자열로 변환하여 출력
        return
    
    for i in range(a, n+1):
        arr.append(i)  # 현재 숫자 i를 선택
        dfs(i) 
        arr.pop()  # 백트래킹

dfs(1)
