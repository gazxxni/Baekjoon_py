n = int(input())
arr = list(map(int, input().split()))
m = int(input())
brr = list(map(int, input().split()))

dic = {}
for i in range(len(arr)):
    dic[arr[i]] = 0

ans = []
for i in range(m):
    if brr[i] not in dic:
        ans.append(0)
    else:
        ans.append(1)
        
print(*ans)