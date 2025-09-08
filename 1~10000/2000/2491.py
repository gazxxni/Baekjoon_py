n = int(input())
arr = list(map(int, input().split()))

inc = [1] * n
dec = [1] * n 

for i in range(1, n):
    if arr[i] >= arr[i-1]:  
        inc[i] = inc[i-1] + 1
        
    if arr[i] <= arr[i-1]: 
        dec[i] = dec[i-1] + 1

print(max(max(inc), max(dec)))
