import sys
input = sys.stdin.readline

n = int(input())

stack = []
ans = []
cnt = 1
flag = True

for _ in range(n):
    a = int(input())

    while cnt <= a:
        stack.append(cnt)
        ans.append("+")
        cnt += 1

    if stack[-1] == a:
        stack.pop(-1)
        ans.append("-")

    else:
        flag = False


if flag:
    print(*ans, sep = "\n")
else:
    print("NO")