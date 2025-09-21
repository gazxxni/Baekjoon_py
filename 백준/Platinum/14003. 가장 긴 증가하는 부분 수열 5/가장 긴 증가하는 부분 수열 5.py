import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# tails[k] = 길이 (k+1)인 증가 부분수열의 최소 끝값
# tails_pos[k] = 위 tails[k]를 만든 인덱스
tails = []
tails_pos = []

# prev_idx[i] = arr[i]가 LIS에 포함될 때 바로 이전 원소의 인덱스
prev_idx = [-1] * n

def search(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

for i, x in enumerate(arr):
    j = search(tails, x)

    # j-1 길이의 꼬리에 이어 붙이므로, 경로의 마지막 인덱스를 prev로 기록
    prev_idx[i] = tails_pos[j - 1] if j > 0 else -1

    if j == len(tails):  # 길이 확장
        tails.append(x)
        tails_pos.append(i)
    else:    # 꼬리값 갱신
        tails[j] = x
        tails_pos[j] = i

# 실가장 긴 길이의 마지막 인덱스부터 prev_idx를 따라 역추적
lis_len = len(tails)
k = tails_pos[-1] if tails_pos else -1

seq = []
while k != -1:
    seq.append(arr[k])
    k = prev_idx[k]
seq.reverse()

print(lis_len)
print(*seq)