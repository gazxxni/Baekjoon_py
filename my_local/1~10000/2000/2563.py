import sys
input = sys.stdin.readline

n = int(input())
visited = set()

for _ in range(n):
    x, y = map(int, input().split())
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            visited.add((i, j))

print(len(visited))