n = int(input())

cnt = 0
for _ in range(n):
    string = input().rstrip()
    alpha = set(string[0])
    flag = True
    for i in range(1, len(string)):
        if string[i] in alpha:
            if string[i - 1] != string[i]:
                flag = False
        else:
            alpha.add(string[i])
    
    if flag:
        cnt += 1

print(cnt)