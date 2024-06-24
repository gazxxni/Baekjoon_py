import sys

n,m=map(int,input().split())

board=[]
result=[]

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        a1=0
        a2=0

        for a in range(i,i+8):
            for b in range(j,j+8):
                if(a+b)%2==0:
                    if board[a][b]!='B':
                        a1+=1
                    if board[a][b]!='W':
                        a2+=1
                else:
                    if board[a][b]!='W':
                        a1+=1
                    if board[a][b]!='B':
                        a2+=1
        result.append(a1)
        result.append(a2)
        
print(min(result))