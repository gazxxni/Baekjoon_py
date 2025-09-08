import sys

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()

for i in b:
    x,y=0,n-1
    isExist=False

    while x<=y:
        mid=(x+y)//2
        if i==a[mid]:
            isExist=True
            print(1)
            break
        elif i>a[mid]:
            x=mid+1
        else:
            y=mid-1
    if not isExist:
        print(0)
