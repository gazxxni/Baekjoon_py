import sys

t=int(input())

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

for _ in range(t):
    n,m=map(int,input().split())
    ans=factorial(m)//(factorial(n)*factorial(m-n))
    print(ans)