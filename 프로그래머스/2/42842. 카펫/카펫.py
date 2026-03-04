import math

def solution(brown, yellow):
    ans = []
    total = brown + yellow
    
    def div(n):
        di = []
        
        for i in range(3, int(n ** 0.5) + 1):
            if n % i == 0:
                di.append((i, n // i))

        return di

    arr = div(total)
    for a, b in arr:
        if (a + b - 2) * 2 == brown:
            if a >= b:
                ans.append(a)
                ans.append(b)
            else:
                ans.append(b)
                ans.append(a)
                
    return ans