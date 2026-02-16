from collections import Counter

n, d = map(int, input().split())
arr = []
for i in range(1, n + 1):
    if i < 10:
        arr.append(i)
    elif 10 <= i < 100:
        arr.append(int(str(i)[0]))
        arr.append(int(str(i)[1]))
    elif 100 <= i < 1000:
        arr.append(int(str(i)[0]))
        arr.append(int(str(i)[1]))
        arr.append(int(str(i)[2]))
    elif 1000 <= i < 10000:
        arr.append(int(str(i)[0]))
        arr.append(int(str(i)[1]))
        arr.append(int(str(i)[2]))
        arr.append(int(str(i)[3]))
    elif 10000 <= i < 100000:
        arr.append(int(str(i)[0]))
        arr.append(int(str(i)[1]))
        arr.append(int(str(i)[2]))
        arr.append(int(str(i)[3]))
        arr.append(int(str(i)[4]))
    else:
        arr.append(int(str(i)[0]))
        arr.append(int(str(i)[1]))
        arr.append(int(str(i)[2]))
        arr.append(int(str(i)[3]))
        arr.append(int(str(i)[4]))
        arr.append(int(str(i)[5]))
        
cnt = Counter(arr)
print(cnt[d])


n, d = map(int, input().split())

print(''.join(map(str, range(1, n + 1))).count(str(d)))