n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

ans = 0

for i in range(n):
    x1, y1 = arr[i]
    x2, y2 = arr[(i + 1) % n]
    ans += (x1 * y2) - (x2 * y1)

area = abs(ans) / 2
print(f"{area:.1f}")
