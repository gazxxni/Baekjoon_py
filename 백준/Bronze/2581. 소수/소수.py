m = int(input())
n = int(input())

arr = [True] * 10001
arr[0], arr[1] = False, False

for i in range(2, int(n ** 0.5) + 1): 
    if arr[i]:
        for j in range(i * i, n + 1, i):
            arr[j] = False
             
cnt = 0
ans = 0
for i in range(m, n + 1):
    if arr[i]:
        cnt += i
        if ans == 0:
            ans = i

if ans == 0:
    print(-1)
else:
    print(cnt)
    print(ans)