n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()
a = -1

for i in range(n):
    a = max(a, arr[i] * n)
    n -= 1
    
    
print(a)