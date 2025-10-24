n = int(input())

cnt = 0
arr = set()
for _ in range(n):
    a = input().rstrip()
    if a == 'ENTER':
        cnt += len(arr)
        arr = set()
        continue
    
    arr.add(a)

cnt += len(arr)
print(cnt)