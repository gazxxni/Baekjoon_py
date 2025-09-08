import sys
input = sys.stdin.readline

m = int(input())
MOD = 1000000007

def cal(a, b = MOD - 2):
    result = 1

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return result
    

result = 0

for _ in range(m):
    n, s = map(int, input().split())
    result = (result + (s * cal(n))) % MOD

print(result)