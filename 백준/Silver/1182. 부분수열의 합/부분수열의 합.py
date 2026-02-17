from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0 
combi = [list(combinations(arr, i)) for i in range(1, n + 1)]

for row in combi:
    for c in row:
        if sum(c) == s:
            cnt += 1

print(cnt)