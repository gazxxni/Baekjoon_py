from collections import defaultdict
dic_x = defaultdict(int)
dic_y = defaultdict(int)

for _ in range(3):
    a, b = map(int, input().split())
    
    dic_x[a] += 1
    dic_y[b] += 1
    
for k, v in dic_x.items():
    if v % 2 == 1:
        x = k
for k, v in dic_y.items():
    if v % 2 == 1:
        y = k
           
print(x, y)