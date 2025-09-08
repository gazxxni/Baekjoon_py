import sys

n=int(input())
a=[]

for _ in range(n):
    x, y = input().split()
    a.append([int(x),y])

sorted(a,key=lambda x : x[0])

for i in a:
    print(i[0],i[1])