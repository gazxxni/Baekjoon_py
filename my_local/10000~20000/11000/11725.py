import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
visited = [False] * (n+1)
ans = [0] * (n+1)  # 각 노드의 부모 노드를 저장
arr = [[] for _ in range(n+1)]  # 그래프의 연결 관계를 저장

for i in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)  # a에서 b로 연결
    arr[b].append(a)  # b에서 a로 연결 (양방향 그래프)

def bfs(arr, v, visited):

    q = deque([v])  # 시작 노드를 큐에 넣음
    visited[v] = True  # 시작 노드를 방문 처리
    while q:
        x = q.popleft()  # 큐에서 노드를 꺼냄
        for i in arr[x]:  # 현재 노드 x와 연결된 모든 노드 i를 확인
            if not visited[i]:  # 아직 방문하지 않은 노드라면
                ans[i] = x  # 현재 노드를 i의 부모로 설정
                q.append(i) 
                visited[i] = True 

bfs(arr, 1, visited)

for i in range(2, n+1):
    print(ans[i])
