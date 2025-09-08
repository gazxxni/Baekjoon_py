import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
graph = [[0] * C for _ in range(R)]
sharks = dict()

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1, c-1)] = (s, d, z)
    
cnt = 0

def fishing(i):
    for r, c in sharks.keys():
        if c == i:
            sharks.pop((r, c))
            cnt += 1
            break
        
    for (r, c), (s, d, z) in sharks.items():
        if d == 1:
            if (s // R) % 2 == 0:
                move = s % R
                r -= move
            else:
                d = 2
                
            
    
    
    
print(sharks)