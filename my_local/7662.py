import sys
import heapq

input = sys.stdin.readline

T = int(input()) 

for _ in range(T):
    min_heap = [] 
    max_heap = [] 
    k = int(input())  
    check = [1] * k  # 삽입된 숫자의 유효성 여부를 저장 (1: 유효, 0: 삭제됨)

    for i in range(k):
        cal, num = input().split()  
        num = int(num)  

        if cal == "I": 
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))

        else:  
            if num == -1:
                if min_heap:  # 최소 힙이 비어 있지 않은 경우
                    # 최소 힙에서 가장 작은 값을 제거하고 해당 인덱스를 `check`에서 0으로 표시
                    check[heapq.heappop(min_heap)[1]] = 0
            elif num == 1:
                if max_heap:  # 최대 힙이 비어 있지 않은 경우
                    # 최대 힙에서 가장 큰 값을 제거하고 해당 인덱스를 `check`에서 0으로 표시
                    check[heapq.heappop(max_heap)[1]] = 0

        # 최소 힙에서 이미 삭제된 원소를 제거 (동기화)
        while min_heap and check[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)

        # 최대 힙에서 이미 삭제된 원소를 제거 (동기화)
        while max_heap and check[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)

    if not min_heap: 
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
