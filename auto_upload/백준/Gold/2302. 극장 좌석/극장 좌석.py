import sys

def solve():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    vips = [int(sys.stdin.readline()) for _ in range(m)]

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    if n >= 2:
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

    ans = 1
    current_pos = 0

    for vip in vips:
        length = vip - current_pos - 1
        ans *= dp[length]
        current_pos = vip

    ans *= dp[n - current_pos]
    print(ans)

solve()