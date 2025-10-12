import math
from collections import defaultdict
s = input().rstrip()
dic = defaultdict(int)
for i in range(1, len(s) + 1):
    for j in range(0, len(s)):
        a = s[j:j + i]
        dic[a] += 1
        
print(len(dic))
