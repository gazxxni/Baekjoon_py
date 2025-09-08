import sys

n = int(input())
arr = list(map(int, input().split()))

result = sorted(set(arr))  # 중복 제거 및 정렬

# 딕셔너리를 사용하여 값의 순위를 저장 (해쉬테이블)
rank = {value: idx for idx, value in enumerate(result)}

# arr의 각 값에 해당하는 순위를 저장
for i in range(len(arr)):
    arr[i] = rank[arr[i]]  # 딕셔너리에서 순위 찾기

for i in arr:
    print(i)
