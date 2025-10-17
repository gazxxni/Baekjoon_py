from collections import defaultdict
t = int(input())

for _ in range(t):
    arr = []
    
    for i in range(4):
        x, y = map(int, input().split())
        arr.append((x, y))
    
    dic = defaultdict(int)
    for i in range(4):
        for j in range(4):
            if i != j:
                a = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2
                dic[a] += 1
    
    aa = False
    bb = False  
    for k, v in dic.items():
        if v == 8:
            aa = True
        
        elif v == 4:
            bb = True
            
    if aa and bb:
        print(1)
        
    else:
        print(0)