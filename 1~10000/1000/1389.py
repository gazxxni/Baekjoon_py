import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().strip().split())
graph = [[] for _ in range(n+1)]  # 그래프 초기화

for i in range(m):  # 그래프 생성
    a,b=map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    num=[0]*(n+1)   # start의 케빈 베이컨들
    ch[start]=1     # 시작 부분 방문표시

    Q=deque()
    Q.append(start)

    while Q:
        x=Q.popleft()
        for i in graph[x]:
            if ch[i]==0:  # 찾지 않은 친구인 경우에만
                num[i]=num[x]+1  # 한 번 거칠 때마다 + 1
                ch[i]=1  # 찾았다고 표시
                Q.append(i)
                # 또 해당 친구에서 다른 친구로 갈 수 있는 루트 찾기
                # 어차피 이미 찾은 친구는 표시되어 있으므로
                # 가장 최소값으로 찾아짐

    return sum(num)  # 케빈 베이컨 수의 합

ans=[]

for i in range(1,n+1):
    ch=[0]*(n+1)  # 이미 찾았는지 확인할 리스트
    ans.append(bfs(graph,i))

print(ans.index(min(ans))+1)  # 값이 같은 경우 index(사람의 번호)가 적은 걸로 출력