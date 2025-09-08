import sys

l=int(input())
m=1234567891
r=31
a=input()
answer=0
for i in range(len(a)):
   num=ord(a[i])-96
   answer+=num*(r**i)
print(answer%m)