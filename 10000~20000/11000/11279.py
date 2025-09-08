import sys, heapq

input=sys.stdin.readline

n=int(input())
heap=[]

for _ in range(n):
    x=int(input())
    
    if x>0:
        heapq.heappush(heap,-x)    # 최대 힙에 숫자를 넣는 함수
    elif x==0:
        try:
            print(-(heapq.heappop(heap)))  # 입력된 숫자가 0이면 가장 큰 값 꺼냄
        except:
            print(0)  # 힙이 비어 있는 경우 0을 출력

