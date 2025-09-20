s = list(input().rstrip())
l = len(s)
dic = {}

for i in s:
    dic[i] = dic.get(i, 0) + 1

cnt = 0
def back(dic, before, use):
    global cnt
    if use == l:
        cnt += 1
        return
    
    for k, v in dic.items():
        if v > 0 and k != before:
            dic[k] -= 1
            back(dic, k, use + 1)
            dic[k] += 1

back(dic, None, 0)
print(cnt)
