import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# def lcm(a, b):
#     for i in range(max(a, b), (a * b) + 1):
#         if i % a == 0 and i % b == 0:
#             return i
        
# print(lcm(a, b))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm2(a, b):
    return a * b // gcd(a, b)

print(lcm2(a, b))