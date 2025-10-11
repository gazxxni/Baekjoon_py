from collections import defaultdict

n, m, k = map(int, input().split())
dic = defaultdict(int)

for _ in range(n):
    s, p = map(str, input().split())
    dic[s] = int(p)

ans = 0
for _ in range(k):
    t = input().rstrip()
    ans += dic[t]
    
    dic.pop(t)

dic = sorted(dic.items(), key=lambda item: item[1])
m -= k

max_ans = ans
min_ans = ans
if m > 0:
    a = dic[:m]
    min_ans += sum(item[1] for item in a)
    
    b = dic[-m:]
    max_ans += sum(item[1] for item in b)
    
print(min_ans, max_ans)
