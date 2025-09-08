from collections import defaultdict

n = int(input())

fruit_category = list(map(int, input().split()))

ans = 0 
left = 0  # 슬라이딩 윈도우의 왼쪽 끝을 가리키는 포인터
cnt = {}  # 각 과일의 카테고리별로 몇 개가 있는지 저장하는 딕셔너리
distinct_cnt = 0  # 현재 슬라이딩 윈도우 내에 있는 고유한 과일 종류의 수

# 슬라이딩 윈도우의 오른쪽 끝을 이동하면서 처리
for right in range(n):
    # 현재 과일이 이미 딕셔너리에 있다면, 그 과일의 개수를 증가시킴
    if fruit_category[right] in cnt:
        cnt[fruit_category[right]] += 1
    # 그렇지 않다면, 새로운 과일 종류로 추가하고, 고유 과일 종류의 수 증가
    else:
        cnt[fruit_category[right]] = 1
        distinct_cnt += 1

    # 고유한 과일 종류가 2개를 초과하면, 조건을 만족할 때까지 왼쪽 포인터를 이동
    while distinct_cnt > 2:
        # 왼쪽 포인터가 가리키는 과일의 개수를 1 줄임
        cnt[fruit_category[left]] -= 1
        # 만약 그 과일의 개수가 0이 되면, 딕셔너리에서 해당 과일을 제거하고 고유 과일 수 감소
        if cnt[fruit_category[left]] == 0:
            del cnt[fruit_category[left]]
            distinct_cnt -= 1
        left += 1     # 왼쪽 포인터를 1칸 이동
    
    # 현재 슬라이딩 윈도우 크기 (right - left + 1)와 지금까지의 최대 길이를 비교해 최대값을 업데이트
    ans = max(ans, right - left + 1)

print(ans)

