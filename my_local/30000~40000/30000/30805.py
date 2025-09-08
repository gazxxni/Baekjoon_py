n = int(input())
arr = list(map(int, input().split()))   
m = int(input())
brr = list(map(int, input().split()))

ans = []

def search(arr, brr):
    if not arr or not brr:  # 두 배열 중 하나라도 비어 있으면 결과 반환
        return ans
    
    tmp1, tmp2 = max(arr), max(brr)
    idx1, idx2 = arr.index(tmp1), brr.index(tmp2)

    if tmp1 > tmp2:  # tmp1이 더 크면 arr에서 제거하고 재귀 호출
        arr.pop(idx1)
        return search(arr, brr)
    
    elif tmp1 < tmp2:  # tmp2가 더 크면 brr에서 제거하고 재귀 호출
        brr.pop(idx2)
        return search(arr, brr)
    
    else:  # 두 값이 같으면 결과에 추가하고 그 이후 부분으로 재귀 호출
        ans.append(tmp1)
        return search(arr[idx1 + 1 :], brr[idx2 + 1 :])
    
a = search(arr, brr)

print(len(a))
if a:
    print(*a)