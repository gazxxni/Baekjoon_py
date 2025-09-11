import sys
input = sys.stdin.readline

'''
두 수의 차가 D로 나누어 떨어진다
(aᵢ - aⱼ) % D = 0 -> 성립해야함

따라서 |a₂ - a₁|, |a₃ - a₁|, ..., |aₙ - a₁|
이 숫자들의 최대공약수를 구해야함
'''

n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        
    return a

brr = list(set(arr))
crr = []

for i in range(len(brr) - 1):
    for j in range(i + 1, len(brr)):
        crr.append(abs(brr[j] - brr[i])) 
        
ans = crr[0]
for i in range(1, len(crr)): 
    ans = gcd(ans, crr[i])
    
print(ans)