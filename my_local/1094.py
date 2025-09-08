import sys

x=int(input())

arr = [64, 32, 16, 8, 4, 2, 1]
cnt = 0

for i in range(len(arr)):
    if x >= arr[i]:
        cnt += 1
        x -= arr[i]

    if x == 0:
        break

print(cnt)
