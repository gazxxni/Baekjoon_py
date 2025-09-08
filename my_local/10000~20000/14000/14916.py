import sys
input = sys.stdin.readline

n = int(input())

five = n // 5

while True:
    money = n - 5 * five
    
    if money % 2 == 0:
        two = money // 2
        print(five + two)
        break
    
    else:
        five -= 1
        
        if five < 0:
            print(-1)
            break