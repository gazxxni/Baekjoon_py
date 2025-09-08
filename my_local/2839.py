import sys

n=int(input())

if n%5==0:
    print(n//5)
else:
    a=0
    while n>0:
        n-=3
        a+=1
        if n%5==0:
            a+=n//5
            print(a)
            break
        elif n==1 or n==2:
            print(-1)
        elif n==0:
            print(a)
            break