import sys

s=set()
input=sys.stdin.readline

m=int(input())

for _ in range(m):
    a=input().strip().split()

    if len(a)==1:
        if a[0]=="all":
            s=set([i for i in range(1,21)])
        else:
            s=set()

    else:
        func,x=a[0],a[1]
        x=int(x)

        if func=='add':
            s.add(x)
        elif func=='remove':
            s.discard(x)
        elif func=='check':
            print(1 if x in s else 0)
        elif func=='toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)

                