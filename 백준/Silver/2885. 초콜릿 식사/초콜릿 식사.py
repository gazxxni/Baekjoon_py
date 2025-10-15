k = int(input())

cnt = 0
a = 1
while True:
  if a >= k:
      break
  
  a *= 2
  cnt += 1   

if k % 2 == 1:
    print(a, cnt)
    
elif k == a:
    print(a, 0)
    
else:
    cnt2 = 0
    ans = a
    while k > 0:
        if k >= a:
            k -= a
        else:
            a //= 2
            cnt2 += 1
    print(ans, cnt2)