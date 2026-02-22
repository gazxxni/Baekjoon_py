from itertools import permutations

n = int(input())
num = list(map(int, input().split()))
p, m, t, d = map(int, input().split())

min_ans = float('inf')
max_ans = float('-inf')

arr = ['+' * p + '-' * m + '*' * t + '/' * d]

per = list(permutations(arr[0], n - 1))

for i in per:
    ans = num[0]
    
    for j in range(n - 1):
        if i[j] == '+':
            ans += num[j + 1]
        elif i[j] == '-':
            ans -= num[j + 1]
        elif i[j] == '*':
            ans *= num[j + 1]
        else:
            if ans < 0:
                ans = -(-ans // num[j + 1])
            else:
                ans //= num[j + 1]
    
    min_ans = min(min_ans, ans)
    max_ans = max(max_ans, ans)


print(max_ans)
print(min_ans)