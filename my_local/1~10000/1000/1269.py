a, b = map(int, input().split())
arr = set(list(map(int, input().split())))
brr = set(list(map(int, input().split())))

crr = arr - brr
drr = brr - arr

print(len(crr) + len(drr))