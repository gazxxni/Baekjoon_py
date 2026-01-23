t = int(input())

for i in range(t):
    input()
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    
    arr.sort()
    brr.sort()
    
    while arr and brr :	
        if arr[0] >= brr[0] :	
            brr.pop(0)
        else :
            arr.pop(0)

    if arr :
        print('S')
    elif brr :
        print('B')
    else :
        print('C')