import sys

n,k=map(int,sys.stdin.readline().split())
idx=0
queue=[i for i in range(1,n+1)]
a=[]

while queue:
    idx+=k-1
    if idx>=len(queue):
        idx%=len(queue)
    a.append(str(queue.pop(idx)))

print("<", ", ".join(a),">",sep="")