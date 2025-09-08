import sys

input = sys.stdin.readline

n=int(input())
stack=[]

my_sum=0
cnt=dict()

for _ in range(n):
    a=int(input())
    stack.append(a)

    my_sum+=a

    if a not in cnt:
        cnt[a]=1
    else:
        cnt[a]+=1

stack.sort()

print(round(my_sum/n))
print(stack[n//2])

freq=max(cnt.values())
number=[]

for key,value in cnt.items():
    if value == freq:
        number.append(key)

if len(number) ==1:
    print(number[0])
else:
    print(sorted(number)[1])

print(stack[-1]-stack[0])

