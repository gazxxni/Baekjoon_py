import sys

n,k=map(int,input().split())
a=[]
cnt=0

for i in range(n):
    a.append(int(input()))

a.reverse()

for i in a:
    cnt+=k//i
    k%=i

print(cnt)


