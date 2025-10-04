a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

f = a1 * n + a0
g = c * n

if f <= g and  a1 <= c:
    print(1)

else:
    print(0)