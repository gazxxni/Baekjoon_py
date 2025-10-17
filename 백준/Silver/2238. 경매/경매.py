import sys
input = sys.stdin.readline

u, n = map(int, input().split())
m = 10001
arr = [[] for _ in range(m)]
brr = [0 for _ in range(m)]
max_num = m

for _ in range(n):
    s, p = input().split()
    p = int(p)
    arr[p].append(s) 
    brr[p] += 1

for i in range(m): 
    if brr[i] != 0:  
        max_num = min(brr[i], max_num)
        
for i in range(m): 
    if max_num == brr[i]:
        print(arr[i][0], i)
        break