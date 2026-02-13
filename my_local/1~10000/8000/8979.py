n, k =map(int, input().split())
medal = [list(map(int, input().split())) for _ in range(n)]

medal.sort(reverse=True, key=lambda x:(x[1], x[2], x[3]))

grade = 1
medal[0].append(grade)
gold = medal[0][1]
silver = medal[0][2]
copper = medal[0][3]
cnt = 0
for i in range(1, n):
    if gold == medal[i][1] and silver == medal[i][2] and copper == medal[i][3]:
        medal[i].append(grade)
        cnt += 1
    else:
        grade += 1 + cnt
        cnt = 0
        medal[i].append(grade)
        gold = medal[i][1]
        silver = medal[i][2]
        copper = medal[i][3]

for i in range(n):
    if medal[i][0] == k:
        print(medal[i][4])
        break