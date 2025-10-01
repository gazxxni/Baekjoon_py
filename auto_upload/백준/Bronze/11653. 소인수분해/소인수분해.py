import sys
import math
input = sys.stdin.readline

n = int(input())

while n % 2 == 0:
    print(2)
    n //= 2

for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        print(i)
        n //= i

if n > 1:
    print(n)