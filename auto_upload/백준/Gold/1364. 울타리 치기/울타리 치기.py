n = int(input())

cnt = 0

if n % 6 == 0:
    cnt += 1
    
while n > 0:
    cnt += n
    n -= 6

print(cnt)