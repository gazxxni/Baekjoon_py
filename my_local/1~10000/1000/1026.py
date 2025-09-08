n = int(input())

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

arr.sort()
brr.sort(reverse=True)

a = 0
for i in range(n):
    a += arr[i] * brr[i]
    
print(a)