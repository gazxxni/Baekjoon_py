n = int(input())
arr = list(map(int, input().split()))

def search(n, arr):
    dp_inc = [1] * n   # 증가하는 부분 수열 (LIS)
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)

    dp_dec = [1] * n   # 감소하는 부분 수열 (LDS) (역순으로 LIS 구하기)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)
                
    # -1을 하는 이유는 중앙에 있는 원소가 중복 포함되기 때문.
    max_length = max(dp_inc[i] + dp_dec[i] - 1 for i in range(n)) 
    
    return max_length

print(search(n, arr))