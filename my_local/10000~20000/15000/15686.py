import sys
input = sys.stdin.readline

n, m = map(int, input().split())
house = []  
chicken = [] 

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            house.append((i, j)) 
        elif arr[j] == 2:
            chicken.append((i, j)) 

result = float('inf')
selected = [] 

def chicken_dist():
    total_distance = 0

    # 모든 집에 대해 가장 가까운 치킨집과의 거리 계산
    for hx, hy in house:
        min_distance = float('inf')
        for cx, cy in selected:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += min_distance

    return total_distance

def dfs(idx, cnt):
    global result

    # 만약 m개의 치킨집을 선택했다면 최소 거리 갱신
    if cnt == m:
        result = min(result, chicken_dist())
        return

    for i in range(idx, len(chicken)):
        selected.append(chicken[i])  # 치킨집 선택
        dfs(i + 1, cnt + 1)  # 다음 치킨집 선택
        selected.pop()  # 백트래킹 (선택 해제)

dfs(0, 0)
print(result)
