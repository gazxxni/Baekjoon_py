x, y = map(int, input().split())

arr = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
brr = [31,28,31,30,31,30,31,31,30,31,30,31]

day = 0

for i in range(x - 1):
    day += brr[i]
    
ans = (day + y) % 7
print(arr[ans])
