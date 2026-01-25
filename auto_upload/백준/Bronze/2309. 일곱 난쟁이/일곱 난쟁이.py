arr = [int(input()) for _ in range(9)]
arr.sort()

sum_arr = sum(arr)
target = sum_arr - 100

fake1 = 0
fake2 = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            fake1 = arr[i]
            fake2 = arr[j]
            break
    if fake1 != 0:
        break

for i in arr:
    if i != fake1 and i != fake2:
        print(i)