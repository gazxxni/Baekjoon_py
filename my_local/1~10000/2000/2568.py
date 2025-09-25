import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()
brr = []
for a, b in arr:
    brr.append(b)

tails = []
tails_pos = []

prev_idx = [-1] * n

def search(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

for i, x in enumerate(brr):
    j = search(tails, x)

    prev_idx[i] = tails_pos[j - 1] if j > 0 else -1

    if j == len(tails): 
        tails.append(x)
        tails_pos.append(i)
    else:    
        tails[j] = x
        tails_pos[j] = i

lis_len = len(tails)
k = tails_pos[-1] if tails_pos else -1

keep = [False] * n
k = tails_pos[-1] if tails_pos else -1
while k != -1:
    keep[k] = True
    k = prev_idx[k]
    
ans = [arr[i][0] for i in range(n) if not keep[i]]
ans.sort()
        
print(n - lis_len)
for a in ans:
    print(a)