import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())

arr = [[] for _ in range(n)]
indegree = [0] * n
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)  
    indegree[b-1] += 1

def topological_sort():    
    hq = []

    for i in range(n):
        if indegree[i] == 0:
            heapq.heappush(hq, i)
            
    while hq:
        cur = heapq.heappop(hq)
        ans.append(cur)
        
        for j in arr[cur]:
            indegree[j] -= 1
            
            if indegree[j] == 0:
               heapq.heappush(hq, j)
                
            
    return ans

topological_sort()
for i in ans:
    print(i+1, end=' ')
