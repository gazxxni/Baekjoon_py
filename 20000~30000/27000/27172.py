import sys
input = sys.stdin.readline

MAX = 1000000

n = int(input())
arr = list(map(int, input().split()))

set_arr = set(arr)
ans = dict.fromkeys(arr, 0)

for i in arr:
    j = i * 2
    while j <= MAX:
        if j in set_arr:
            ans[i] += 1       
            ans[j] -= 1   
        j += i

print(*[ans[x] for x in arr])
