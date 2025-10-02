import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())


if a == b == c == 60:
    print('Equilateral')

elif a + b + c == 180:
    if a == b and b != c:
        print('Isosceles')
    elif a == c and b != c:
        print('Isosceles')
    elif b == c and a != c:
        print('Isosceles')
    else:
        print('Scalene')

else:
    print('Error')