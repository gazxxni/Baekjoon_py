import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

arr = []
brr = []

for i in range(n): 
    sum = 0
    for j in range(i, n): 
        sum += A[j]
        arr.append(sum)

for i in range(m): 
    sum = 0
    for j in range(i, m): 
        sum += B[j]
        brr.append(sum)

arr.sort()
brr.sort(reverse=True)

i, j = 0, 0
result = 0

while i < len(arr) and j < len(brr):
    current = arr[i] + brr[j]

    if current == t:
        aa = arr[i]
        bb = brr[j]
        a_cnt = b_cnt = 0

        while i < len(arr) and arr[i] == aa:
            a_cnt += 1
            i += 1

        while j < len(brr) and brr[j] == bb:
            b_cnt += 1
            j += 1

        result += a_cnt * b_cnt

    elif current < t:
        i += 1
    else:
        j += 1

print(result if result > 0 else -1)



# =============================================================
# Counter 방식

# from collections import Counter

# t = int(input())
# n = int(input())
# A = list(map(int, input().split()))
# m = int(input())
# B = list(map(int, input().split()))

# arr, brr = [], []

# for i in range(n): 
#     sum = 0
#     for j in range(i, n): 
#         sum += A[j]
#         arr.append(sum)

# for i in range(m): 
#     sum = 0
#     for j in range(i, m): 
#         sum += B[j]
#         brr.append(sum)

# # B의 부분합 빈도 저장
# b_counter = Counter(brr)

# # A 부분합과 T - a 를 만족하는 b의 개수 세기
# result = 0
# for a in arr:
#     result += b_counter[t - a]

# print(result)
