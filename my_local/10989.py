import sys

# 메모리 초과
# n=int(sys.stdin.readline())
# a=[]

# for _ in range(n):
#     a.append(int(sys.stdin.readline()))
    
# sorted_a=sorted(a)

# for i in sorted_a:
#     print(i)

n=int(sys.stdin.readline())
a=[0]*10001

for _ in range(n):
    a[int(sys.stdin.readline())]+=1

for i in range(10001):
    if a[i]!=0:
        for j in range(a[i]):
            print(i)