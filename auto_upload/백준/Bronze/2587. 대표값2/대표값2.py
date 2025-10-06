import sys

arr = []
cnt = 0
for i in range(5):
    a = int(input())
    arr.append(a)
    cnt += a

ave = cnt // 5

arr.sort()

print(ave)
print(arr[2])
