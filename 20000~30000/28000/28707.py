import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
brr = []
for _ in range(m):
    l, r, c = map(int, input().split())
    brr.append((l-1, r-1, c))
    
start = tuple(arr)
goal = tuple(sorted(arr))
visited = {}

def dijk():
    heap = []
    heapq.heappush(heap, (0, start))
    visited[start] = 0
    
    while heap:
        cost, state = heapq.heappop(heap)
        
        if state == goal:
            print(cost)
            break
        
        if visited[state] < cost:
            continue
        
        for l, r, c in brr:
            
            new_state = list(state)
            new_state[l], new_state[r] = new_state[r], new_state[l]
            next_state = tuple(new_state)
            new_cost = cost + c
            
            if next_state not in visited or visited[next_state] > new_cost:
                visited[next_state] = new_cost
                heapq.heappush(heap, (new_cost, next_state))
            
    else:
        print(-1)        
                
dijk()