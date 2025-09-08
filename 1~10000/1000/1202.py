import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jew = []
for _ in range(n):
    m, v = map(int, input().split())
    jew.append((m, v))
    
bag = [int(input()) for _ in range(k)]

jew.sort()
bag.sort()

heap = []
value = 0
jew_idx = 0

for i in bag:
    
    while jew_idx < n and jew[jew_idx][0] <= i:
        heapq.heappush(heap, -jew[jew_idx][1])
        jew_idx += 1
        
    if heap:
        value += -heapq.heappop(heap)
        
        
print(value)