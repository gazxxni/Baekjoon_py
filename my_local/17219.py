import sys

input = sys.stdin.readline

n, m = map(int, input().split())
password = {}

for _ in range(n):
    site, pw = input().split()
    password[site] = pw

for _ in range(m):
    print(password[input().rstrip()])