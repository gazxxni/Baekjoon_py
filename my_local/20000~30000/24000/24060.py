def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global cnt, ans
    
    i = p
    j = q + 1
    t = 0
    tmp = [0] * (r - p + 1)
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1
        
    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1
        
    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1
        
    i = p
    t = 0
    
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        
        if cnt == k:
            ans = A[i]
            
        i += 1
        t += 1

n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
ans = -1

merge_sort(arr, 0, n - 1)

print(ans)