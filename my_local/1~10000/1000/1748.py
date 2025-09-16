import sys
input = sys.stdin.readline

n = input().rstrip()
l = len(n)

ans = 0
for i in range(1, l):
    ans += 9 * (10 ** (i - 1)) * i
    
ans += (int(n) - (10 ** (l - 1)) + 1) * l
print(ans)