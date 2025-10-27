n, m = map(int, input().split())
arr = []

def aa():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            aa()
            arr.pop()
            
aa()