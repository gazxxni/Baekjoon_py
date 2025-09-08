import sys

n, m = map(int, input().split())  
arr = list(map(int, input().split()))  
arr.sort()  
ans = [] 
visited = [False] * n 


def dfs():
    if len(ans) == m: 
        print(*ans) 
        return 
    
    check = 0  # 같은은 숫자가 사용되는 것을 방지하기 위한 변수

    for i in range(n):
        # 숫자가 아직 방문되지 않았고, 이전에 사용한 숫자가 아닌 경우
        if not visited[i] and check != arr[i]: 
            visited[i] = True  # 현재 숫자를 방문 처리
            ans.append(arr[i])  # 숫자를 결과 리스트에 추가
            check = arr[i]  # 현재 숫자를 중복 체크 변수에 저장
            dfs() 
            visited[i] = False  # 재귀 호출이 끝나면 현재 숫자의 방문을 취소
            ans.pop()  # 결과 리스트에서 숫자를 제거 (백트래킹)

dfs()
