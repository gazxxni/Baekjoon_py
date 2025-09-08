import sys, math
input = sys.stdin.readline

n = input().rstrip()
arr = list(map(int, n)) 
dic = {i:0 for i in range(10)}

for i in arr:
    dic[i] += 1

ans = 0 
for k, v in dic.items():
    if k == 6 or k == 9:
        continue
    
    ans = max(ans, v)

a = int(math.ceil((dic[6] + dic[9]) / 2))
print(max(ans, a))