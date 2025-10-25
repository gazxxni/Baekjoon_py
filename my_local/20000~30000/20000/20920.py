import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())

dic = defaultdict(int)
for _ in range(n):
    a = input().rstrip()
    if len(a) >= m:
        dic[a] += 1
    
dic2 = defaultdict(list)
for k, v in dic.items():
    dic2[v].append(k)
    
for k, v in dic2.items():
    v.sort(key=lambda x: (-len(x), x))
    
a = sorted(dic2.items(), key=lambda x:x[0], reverse=True)

for i, j in a:
    for k in j:
        print(k)