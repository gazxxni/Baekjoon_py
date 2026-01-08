dic = {'black' : 0,
       'brown' : 1,
       'red' : 2,
       'orange' : 3,
       'yellow' : 4,
       'green' : 5,
       'blue' : 6,
       'violet' : 7,
       'grey' : 8,
       'white' : 9
       }

ans = ''
for i in range(3):
    a = input().rstrip()
    
    if i < 2:
        ans += str(dic[a])

    if i == 2:
        ans = int(ans) * (10 ** dic[a])
        
print(ans)