import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    check = [0] * (n + 1)
    res = 0

    for i in range(1, n + 1):
        if check[i] != 0:
            continue

        cur = i

        while check[cur] == 0:
            check[cur] = 1
            cur = arr[cur]

        if check[cur] == 1:
            cycle_start = cur
            cnt = 1
            nxt = arr[cur]

            while nxt != cycle_start:
                cnt += 1
                nxt = arr[nxt]

            res += cnt

        cur = i

        while check[cur] == 1:
            check[cur] = 2
            cur = arr[cur]

    print(n - res)