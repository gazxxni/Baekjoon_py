import sys
input = sys.stdin.readline

alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

a = list(input().rstrip())
b = []
ans = ''

aa = False

for i in a:
    

    if i in alphabet:
        ans += i

    else:
        if i == '(':
            b.append(i)

        elif i == '*' or i == '/':
            while b and b[-1] in ('*', '/'):
                ans += b.pop()
            b.append(i)
        
        elif i == '+' or i == '-':
            while b and b[-1] in ('*', '/', '+', '-'):
                ans += b.pop()
            b.append(i)

        elif i == ')':
            while b and b[-1] != '(':
                ans += b.pop()
            b.pop()

while b:
    ans += b.pop()
print(ans)
