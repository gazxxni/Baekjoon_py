n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]

def greedy(a, b):
    aa = a // b
    bb = a % b

    result = [aa] * b
    for i in range(b):
        if ord(arr[i + 1][0]) >= 97 and bb > 0:
            result[i] += 1
            bb -= 1
    
    for i in range(b - 1, 0, -1):
        if result[i] == aa and bb > 0:
            result[i] += 1
            bb -= 1

    result2 = ["_" * x for x in result]
    return result2

total = 0
for i in range(n):
    total += len(arr[i])

result = greedy(m - total, n- 1)

ans = [arr.pop(0)]
for i in range(n - 1):
    ans.append(result[i])
    ans.append(arr[i])

print(*ans, sep = '')