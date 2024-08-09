import sys

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    imp=list(map(int, input().split()))

    result=1

    while imp:
        if imp[0]<max(imp):
            imp.append(imp.pop(0))

        else:
            if m==0:
                break

            imp.pop(0)
            result +=1

        m = m - 1 if m > 0 else len(imp) - 1

    print(result)

    