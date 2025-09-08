import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

# 끝나는 시간을 기준으로 오름차순 정렬, 끝나는 시간이 같으면 시작 시간 기준으로 정렬
arr.sort(key=lambda x: (x[1], x[0]))

# 첫 번째 회의를 선택했으므로 카운터를 1로 설정
cnt = 1

# 첫 번째 회의의 종료 시간을 imp에 저장
imp = arr[0][1]

# 두 번째 회의부터 차례로 확인
for i in range(1, n):
    # 현재 회의의 시작 시간이 이전 회의의 종료 시간 이후일 경우에만 선택
    if arr[i][0] >= imp:
        imp = arr[i][1]  # imp에 현재 회의의 종료 시간을 저장
        cnt += 1

print(cnt)
