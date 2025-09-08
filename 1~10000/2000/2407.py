n, m = map(int, input().split())

a = 1
arr = [0]
for i in range(1, 101):
    a *= i
    arr.append(a)

print(arr[n] // (arr[n - m] * arr[m]))


# if (n // 2) <= (n - m):
#     print(arr[n] // arr[m])
# else:
#     print(arr[n] // arr[n - m])
    
