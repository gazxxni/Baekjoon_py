import sys
input = sys.stdin.readline

n = int(input())
arr = [True] * 10000001
arr[0], arr[1] = False, False

for i in range(2, int(n ** 0.5) + 1): 
    if arr[i]:
        for j in range(i * i, n + 1, i):
            arr[j] = False

brr = []           
for i in range(n):
    if arr[i]:
        brr.append(i)

a = 0

if n == 2:
    print(2)
    exit()
elif n == 3:
    print(3)
    exit()
    
while True:
    if n % brr[a] == 0:
        n /= brr[a]
        print(brr[a])
        
    else:
        a += 1
        
    if n == 1:
        break