while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        exit()
        
    a, b, c = sorted((a, b, c))
    if c >= a + b:
        print('Invalid')       
    
    elif a == b and b == c:
        print('Equilateral')
        
    elif a == b or b == c or a == c:
        print('Isosceles')
        
    else:
        print('Scalene')