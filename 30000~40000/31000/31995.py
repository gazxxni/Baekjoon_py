import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

check = [arr[i] < arr[i+1] for i in range(n-1)]

ans = n
t = 0
for b in check:
    if b:
        t += 1
    else:
        ans += t * (t + 1) // 2
        t = 0
ans += t * (t + 1) // 2 

print(ans)
