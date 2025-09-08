import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

def search(arr):
    closest = float('inf')
    result = ()

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if abs(total) < abs(closest):
                closest = total
                result = (arr[i], arr[left], arr[right])

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                return 0, (arr[i], arr[left], arr[right])

    return closest, result

_, (a, b, c) = search(arr)
print(a, b, c)