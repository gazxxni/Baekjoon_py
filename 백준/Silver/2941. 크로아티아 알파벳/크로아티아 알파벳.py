arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input().rstrip()

cnt = 0
idx = 0
while idx <= len(string) - 1:
    if string[idx:idx + 3] in arr:
            cnt += 1
            idx += 3
            
    elif string[idx:idx + 2] in arr:
            cnt += 1
            idx += 2
        
    else:
        cnt += 1
        idx += 1
            
print(cnt)