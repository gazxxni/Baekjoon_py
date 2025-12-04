import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

cnt = 0

while True:
    if len(arr) == 1:
        break
    
    arr.sort(reverse=True)
    arr[0] -= arr[1]
    cnt += arr[1]
    arr.pop(1)
    
cnt += arr[0]
if cnt > 1440:
    print(-1)
else:
    print(cnt)