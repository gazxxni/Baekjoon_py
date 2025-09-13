import sys, math
input = sys.stdin.readline

result = [] 
visited = [] 

def backtrack(arr, path):
    if len(path) == len(arr):
        result.append("".join(path))
        return
    
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            backtrack(arr, path + [arr[i]])
            visited[i] = False

while True:
    try:
        a, b = input().split()
        b = int(b)
        a = list(a)
        n = len(a)
        total = math.factorial(n)

        if b > total:
            print(f"{''.join(a)} {b} = No permutation")
            continue

        result = []
        visited = [False] * n
        backtrack(a, [])

        result.sort()
        if b <= total // 2:
            ans = result[b-1]
        else:
            ans = result[-(total-b+1)]

        print(f"{''.join(a)} {b} = {ans}")
        
    except:
        break
