n = int(input())
arr = list(map(int, input().split()))

brr = []
idx = 1

for i in arr:
    if i == idx:
        idx += 1
        while brr and brr[-1] == idx:
            brr.pop()
            idx += 1
    else:
        brr.append(i)

if not brr:
    print("Nice")
else:
    print("Sad")