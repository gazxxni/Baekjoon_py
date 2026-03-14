def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num

        binary = ""
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        s = binary
        
    return [a, b]