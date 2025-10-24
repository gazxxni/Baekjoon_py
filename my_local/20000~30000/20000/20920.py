import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())

dic = defaultdict(int)
for _ in range(n):
    a = input().rstrip()
    dic[a] += 1
    
a = sorted(dic.items(), key=lambda x:x[1], reverse=True)
