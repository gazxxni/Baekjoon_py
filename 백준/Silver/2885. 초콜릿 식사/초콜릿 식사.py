k = int(input())

cnt = 0
a = 1
while True:
  if a >= k:
      break
  
  a *= 2
 

cnt2 = 0
ans = a
while k > 0:
    if k >= a:
        k -= a
    else:
        a //= 2
        cnt2 += 1
print(ans, cnt2)