n, m = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

crr = arr + brr
crr.sort()
print(*crr)