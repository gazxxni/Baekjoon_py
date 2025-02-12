import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n//2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(multi(a, b))




"""
A^m+n = A^m x A^n
(AxB)%C = (A%C) * (B%C) % C
(A^B)%C = (A^(B//2) * A^(B//2)) % C  (B 짝수)
        = (A^(B//2) * A^(B//2) * A) % C  (B 홀수)
"""