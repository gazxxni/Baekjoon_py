import sys
input = sys.stdin.readline

a = int(input())
x = int(input())
MOD = 1_000_000_007

result = 1
a %= MOD

while x > 0:
    if x % 2 == 1: 
       result = (result * a) % MOD
    a = (a * a) % MOD
    x //= 2
    
print(result % MOD)