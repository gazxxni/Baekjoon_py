import sys, heapq

input=sys.stdin.readline

n=int(input())
heap=[]

for _ in range(n):
    arr=int(input())
    
    if arr!=0:
        heapq.heappush(heap,arr)  # 최소 힙에 숫자를 넣는 함수
    else:
        try:
            print(heapq.heappop(heap))  # 입력된 숫자가 0이면 가장 작은 값 꺼냄
        except:
            print(0)  # 힙이 비어 있는 경우 0을 출력

        

    
    
