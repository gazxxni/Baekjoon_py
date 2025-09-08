n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
mod = 1000  

def mul(A, B):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
    return result

def mat_pow(a, b):
    if b == 1:
        for x in range(len(a)):
            for y in range(len(a)):
                a[x][y] %= mod
        return a
    
    if b % 2 == 0:
        half = mat_pow(a, b // 2)
        return mul(half, half)
    else:
        return mul(a, mat_pow(a, b - 1))

result = mat_pow(a, b)
for row in result:
    print(" ".join(map(str, row)))



