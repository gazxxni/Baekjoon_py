import sys

input=sys.stdin.readline

n=int(input())
a=[]

for i in range(n):
    a.append(input())
a.sort()

for j in a:
    print(j)

