import sys

arr = list(input())
ans = []
tmp = []

# 첫 번째 나누는 지점 i를 1부터 len(arr) - 1까지 반복
for i in range(1, len(arr) - 1):
    # 두 번째 나누는 지점 j를 i+1부터 len(arr)까지 반복
    for j in range(i + 1, len(arr)):
        # 문자열을 세 부분으로 나누기
        a = arr[:i]   
        b = arr[i:j] 
        c = arr[j:] 

        a.reverse()
        b.reverse()
        c.reverse()

        tmp.append(a + b + c)

# tmp에 있는 각 리스트 요소를 문자열로 변환하여 ans 리스트에 추가
for i in tmp:
    ans.append(''.join(i))

print(sorted(ans)[0])
