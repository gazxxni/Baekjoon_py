import sys
from collections import Counter

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 2차원 배열을 1차원으로 변환 후 각 높이별 블록 수 계산
flattened_blocks = [block for row in arr for block in row]
block_count = Counter(flattened_blocks)

# 2차원 배열의 최소 높이와 최대 높이 구하기
min_height = min(block_count)
max_height = max(block_count)

# 결과 저장할 변수 (최소 시간, 목표 높이)
best_time = float('inf')
best_height = -1

# 각 목표 높이별로 블록 추가/제거 계산
for target_height in range(min_height, max_height + 1):
    time = 0
    inventory = b

    # 높이별로 블록을 추가하거나 제거하는데 걸리는 시간 계산
    for height, count in block_count.items():  # height: 현재 블록의 높이, count: 해당 높이의 블록 개수
        if height > target_height:  # 블록을 제거해야 하는 경우
            time += (height - target_height) * 2 * count  # 제거는 2초
            inventory += (height - target_height) * count  # 제거된 블록 수 추가
        elif height < target_height:  # 블록을 추가해야 하는 경우
            time += (target_height - height) * count  # 추가는 1초
            inventory -= (target_height - height) * count  # 인벤토리에서 블록 감소

    # 블록 인벤토리가 충분한 경우에만 결과 업데이트
    if inventory >= 0:
        # 최소 시간을 업데이트하되, 시간이 같다면 더 높은 높이를 선택
        if time < best_time or (time == best_time and target_height > best_height):
            best_time = time
            best_height = target_height

# 결과 출력
print(best_time, best_height)
