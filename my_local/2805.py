import sys

input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

start, end=1, max(arr)   # 초기 시작과 끝 값 설정

while start <= end:
    sum=0
    mid=(start+end)//2   # 중간값 설정

    for i in arr:
        if i>mid:
            sum+= i-mid   # 중간값을 기준으로 잘랐을 때 나무 길이 합
        
    if sum<m:       # 가져갈 수 있는 나무 길이 합이 목표보다 작은 경우
        end=mid-1   # 높이를 낮춰야 함
    else:
        start=mid+1

print(end)

