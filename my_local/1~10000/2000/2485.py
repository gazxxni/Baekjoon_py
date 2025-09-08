import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

brr = [arr[i+1] - arr[i] for i in range(n - 1)]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a) 

def gcd_of_array(brr):
    result = brr[0]
    for num in brr[1:]:
        result = gcd(result, num)
        if result == 1:
            return 1
    return result

a = gcd_of_array(brr)

cnt = (arr[-1] - arr[0]) // a + 1 - n
        
print(cnt)