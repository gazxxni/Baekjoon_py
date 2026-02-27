a, b = map(int, input().strip().split(' '))


for i in range(b):
    ans = ''
    for j in range(a):
        ans += '*'
    print(ans)