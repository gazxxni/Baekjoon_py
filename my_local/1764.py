import sys

n,m=map(int,input().split())

a=set()
for i in range(n):
    a.add(input())

b=set()
for i in range(m):
    b.add(input())

ans=sorted(list(a&b))

print(len(ans))

for i in ans:
    print(i)

    