from collections import defaultdict

n = int(input())
dic = defaultdict(int)
for i in range(n):
    _, extend = input().split('.') 
    dic[extend] += 1

for key in sorted(dic.keys()):
    print(key, dic[key])