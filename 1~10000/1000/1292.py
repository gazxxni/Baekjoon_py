a, b = map(int, input().split())

arr = [0]
num = 1

while True:
    if num == 1001:
        break
    
    for _ in range(num):
        arr.append(num)
        
    num += 1

a = sum(arr[a:b+1])
print(a)