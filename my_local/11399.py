import sys

n=int(input())
a=list(map(int,input().split()))

a.sort()

cnt=0
ans=0
for i in a:
    cnt+=i
    ans+=cnt

print(ans)

