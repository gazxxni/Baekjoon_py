import sys

s = sys.stdin.readline().rstrip()
ans = ""
i = 0

while i < len(s):
    if s[i] == '<':
        j = s.find('>', i)
        ans += s[i : j + 1]
        i = j + 1
    
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        tmp = s[start:i]
        ans += tmp[::-1]
    
    else:
        ans += s[i]
        i += 1

print(ans)