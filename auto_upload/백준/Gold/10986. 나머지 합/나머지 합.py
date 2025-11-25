import sys
input = sys.stdin.readline

'''
1. 구간 합이 M으로 나누어 떨어진다는 것은 
(prefix_sum[j] - prefix_sum[i-1]) % M == 0이라는 뜻

2. 이 식을 이항하면 prefix_sum[j] % M == prefix_sum[i-1] % M

3. 즉, 누적합을 M으로 나눈 나머지가 같은 인덱스들을 찾으면 됨
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 1. 나머지를 카운트할 배열 또는 딕셔너리 준비
remainder_count = [0] * m

# 2. 누적합 변수 초기화
current_sum = 0

# 3. 나머지가 0인 경우를 미리 카운트
remainder_count[0] = 1 

# 4. 수열을 순회하면서 누적합과 나머지 계산
for x in arr:
    current_sum += x
    r = current_sum % m
    remainder_count[r] += 1

ans = 0
for cnt in remainder_count:
    # 해당 나머지를 가진 누적합의 개수가 2개 이상일 때만 쌍을 만들 수 있음
    if cnt > 1:
        ans += (cnt * (cnt - 1)) // 2

print(ans)