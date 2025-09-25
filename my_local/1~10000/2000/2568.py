import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()

brr = [b for a, b in arr]

tails = []       
tails_idx = []    
pos = [0] * n      
prev_idx = [-1] * n  

def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

for i, x in enumerate(brr):
    j = lower_bound(tails, x) 

    if j > 0:
        prev_idx[i] = tails_idx[j - 1]  
    else:
        prev_idx[i] = -1

    if j == len(tails):
        tails.append(x)
        tails_idx.append(i)
    else:
        tails[j] = x
        tails_idx[j] = i

    pos[i] = j  

lis_len = len(tails)

keep = [False] * n
need = lis_len - 1  
last_b = float('inf')  

for i in range(n - 1, -1, -1):
    if pos[i] == need and brr[i] < last_b:
        keep[i] = True
        last_b = brr[i]
        need -= 1
        if need < 0:
            break

ans = [arr[i][0] for i in range(n) if not keep[i]]
ans.sort()

print(n - lis_len)
for a in ans:
    print(a)
