n = int(input())

arr = []
brr = []
for i in range(n):
    x, y = map(int, input().split())
    
    arr.append(x)
    brr.append(y)
    
print(abs(max(arr) - min(arr)) * abs(max(brr) - min(brr)))