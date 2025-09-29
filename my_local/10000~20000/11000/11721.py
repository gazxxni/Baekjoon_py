n = list(input().rstrip())

a = len(n) // 10
b = len(n) % 10

arr = [[0] * 10 for _ in range(a)]
brr = []

for i in range(a):
    for j in range(10):
        arr[i][j] = n[10 * i + j]
        
for i in range(len(n) - b, len(n)):
    brr.append(n[i])

for row in arr:
    print(*row, sep='')

print(*brr, sep='')