import sys
input = sys.stdin.readline

'''
항상 A+B = -(C+D) 로 식을 맞춘다.
C,D를 순회하며 ab_freq[-(c+d)](= A+B의 빈도)를 누적해 정답을 구한다.
'''
n = int(input())
arr, brr, crr, drr = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr.append(a); brr.append(b); crr.append(c); drr.append(d)

ab_freq = {}
for a in arr:
    for b in brr:
        s = a + b
        ab_freq[s] = ab_freq.get(s, 0) + 1

ans = 0
for c in crr:
    base = -c
    for d in drr:
        ans += ab_freq.get(base - d, 0)

print(ans)
