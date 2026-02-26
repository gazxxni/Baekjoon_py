import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < k:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + second * 2)
        cnt += 1
        
    return cnt