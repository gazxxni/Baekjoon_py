import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
card_num = list(map(int, input().split()))
chulsu = list(map(int, input().split()))

card_num.sort()

def upper_bound(arr, x):
    st, ed = 0, len(arr)
    
    while st < ed:
        mid = (st + ed) // 2
        
        if arr[mid] <= x:
            st = mid + 1
        else:
            ed = mid
            
    return st

parent = list(range(m + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        
    return parent[x]

ans = []

for i in chulsu:
    pos = upper_bound(card_num, i)
    pos = find(pos)  
    
    ans.append(card_num[pos])
    parent[pos] = find(pos + 1)
    
for i in ans:
    print(i)