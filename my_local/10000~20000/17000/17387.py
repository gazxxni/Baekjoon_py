import sys
input = sys.stdin.readline

def ccw(xa, ya, xb, yb, xc, yc):
    cross = (xb - xa) * (yc - ya) - (yb - ya) * (xc - xa)
    return cross

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

o1 = ccw(x1, y1, x2, y2, x3, y3)
o2 = ccw(x1, y1, x2, y2, x4, y4)
o3 = ccw(x3, y3, x4, y4, x1, y1)
o4 = ccw(x3, y3, x4, y4, x2, y2)

if o1 == 0 and o2 == 0 and o3 == 0 and o4 == 0:
    if (x1, y1) > (x2, y2):
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    if (x3, y3) > (x4, y4):
        x3, x4 = x4, x3
        y3, y4 = y4, y3

    
    if max(min(x1,x2), min(x3,x4)) <= min(max(x1,x2), max(x3,x4)):
        if max(min(y1,y2), min(y3,y4)) <= min(max(y1,y2), max(y3,y4)):
            print(1)
            exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()

if o1 * o2 <= 0 and o3 * o4 <= 0:
    print(1)
    exit()
else:
    print(0)
    exit()
