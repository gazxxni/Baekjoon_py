n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
closest_sum = float('inf')
ans = (0, 0)

while left < right:
    total = arr[left] + arr[right]

    if abs(total) < abs(closest_sum):
        closest_sum = total
        ans = (arr[left], arr[right])

    if total > 0:
        right -= 1

    elif total < 0:
        left += 1

    else:
        break

print(ans[0], ans[1])
