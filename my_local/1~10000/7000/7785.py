from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    a, b = map(str, input().rstrip().split())
    
    if b == 'enter':
        dic[a] += 1
        
    else:
        dic[a] -= 1
        
ans = []    
for k, v in dic.items():
    if v == 1:
        ans.append(k)
        
ans.sort(reverse=True)
for i in ans:
    print(i)