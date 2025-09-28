import sys
input = sys.stdin.readline

MOD = 1_000_000_007

graph = [
    [0,1,1,0,0,0,0,0],
    [1,0,1,1,0,0,0,0],
    [1,1,0,1,1,0,0,0],
    [0,1,1,0,1,1,0,0],
    [0,0,1,1,0,1,0,1],
    [0,0,0,1,1,0,1,0],
    [0,0,0,0,0,1,0,1],
    [0,0,0,0,1,0,1,0],
]

d = int(input().strip())

def multiply(A, B):
    result = [[0] * 8 for i in range(8)]
  
    for i in range(8):
        for j in range(8):
            for k in range(8):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= MOD
      
    return result

def cal(A, n):
    if n == 1:
        return A
    cal2 = cal(A, n//2)
    
    if n % 2 == 0:
        return multiply(cal2, cal2)
    else:
        mul2 = multiply(cal2, cal2)
        return multiply(mul2, A)
    
result = cal(graph, d)
print(result[0][0])