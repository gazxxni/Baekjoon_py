import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
bomb_len = len(bomb)
stack = []

for i in range(len(s)):
    stack.append(s[i])
    if s[i] == bomb[-1] and ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

print(''.join(stack) if stack else 'FRULA')
