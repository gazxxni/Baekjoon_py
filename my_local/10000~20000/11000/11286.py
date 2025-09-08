import heapq
import sys

input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
    num = int(input())
    
    if num != 0:
        # (절댓값, 원래 값) 형태로 힙에 삽입
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            # 절댓값이 가장 작은 값을 꺼냄, 절댓값이 같으면 음수가 먼저 나옴
            print(heapq.heappop(heap)[1])
        else:
            print(0)
