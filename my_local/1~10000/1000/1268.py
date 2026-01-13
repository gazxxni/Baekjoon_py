n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
same_class = [set() for _ in range(n)]

for grade in range(5):
    for j in range(n):
        for k in range(n):
            if j != k:
                if arr[j][grade] == arr[k][grade]:
                    same_class[j].add(k)

ans = -1
idx = 0

for i in range(n):
    aa = len(same_class[i])
    if aa > ans:
        ans = aa
        idx = i + 1

print(idx)