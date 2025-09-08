import sys

n=int(input())
cnt=0

while n>0:
    cnt+=n//5
    n//=5

print(cnt)

# a=[]

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# a=factorial(n)
# a.reverse()

# for i in a:
#     if i==0:
#         cnt+=1