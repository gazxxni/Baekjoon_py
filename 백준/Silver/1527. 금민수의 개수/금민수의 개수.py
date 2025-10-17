import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = [[] for _ in range(10)]
brr = [[] for _ in range(10)]
arr[0].append('4')
brr[0].append('7')

for i in range(1,10):
    for j in arr[i - 1]:
        arr[i].append('4' + j)
        arr[i].append('7' + j)
    for k in brr[i - 1]:
        brr[i].append('4' + k)
        brr[i].append('7' + k)

aa = len(str(a))
bb = len(str(b))
cnt = 0
for i in range(10):
    for j in arr[i]:
        if a <= int(j) <= b:
            cnt += 1
    
    for k in brr[i]:
        if a <= int(k) <= b:
            cnt += 1
            
print(cnt)