import math
from collections import defaultdict
s = input().rstrip()
a = set()
for i in range(1, len(s) + 1):
    for j in range(0, len(s)):
        a.add(s[j:j + i])
 
print(len(a))