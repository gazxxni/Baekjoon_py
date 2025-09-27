n, p = map(int, input().split())
w, l, g = map(int, input().split())

person = {}
for _ in range(p):
    name, wl = input().split()
    
    if wl == 'W':
        wl = w
    else:
        wl = -l
    
    person[name] = wl
    
ans = 0
for i in range(n):
    a = input().rstrip()
    
    if a in person.keys():
        ans += person[a]
    
    else:
        ans += -l
    
    if ans < 0:
        ans = 0

    
    if ans >= g:
        print('I AM NOT IRONMAN!!')
        break
    
if ans < g:
    print('I AM IRONMAN!!')