n = int(input())
arr = []

for _ in range(n):
    data = input().split()
    name = data[0]
    ko, en, ma = map(int, data[1:])
    
    arr.append((name, ko, en, ma))
    
arr.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])