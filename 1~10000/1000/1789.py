import sys
input = sys.stdin.readline

s = int(input())

a = ((1 + 8 * s) ** 0.5 - 1) / 2

print(int(a))