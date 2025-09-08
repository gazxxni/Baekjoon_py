import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

brr = []

def search(arr, x):
    st, ed = 0, len(arr)
    while st < ed:
        mid = (st + ed) // 2
        if arr[mid] < x:
            st = mid + 1
        else:
            ed = mid
    return st

for num in arr:
    if not brr or num > brr[-1]:
        brr.append(num)
    else:
        idx = search(brr, num)
        brr[idx] = num

print(len(brr))
