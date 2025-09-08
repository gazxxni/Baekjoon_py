import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# maxDP와 minDP를 초기화 (최대값과 최소값을 저장하는 배열)
maxDP = arr  # 현재까지의 최대값 경로를 저장
minDP = arr  # 현재까지의 최소값 경로를 저장

for _ in range(n-1):
    arr = list(map(int, input().split()))

    # 슬라이딩 윈도우 방식으로 이전 단계의 값(maxDP, minDP)을 사용해 현재 값 계산
    maxDP = [
        arr[0] + max(maxDP[0], maxDP[1]),              # 첫 번째 칸의 최대값
        arr[1] + max(maxDP[0], maxDP[1], maxDP[2]),    # 두 번째 칸의 최대값
        arr[2] + max(maxDP[1], maxDP[2])               # 세 번째 칸의 최대값
    ]
    
    minDP = [
        arr[0] + min(minDP[0], minDP[1]),              # 첫 번째 칸의 최소값
        arr[1] + min(minDP[0], minDP[1], minDP[2]),    # 두 번째 칸의 최소값
        arr[2] + min(minDP[1], minDP[2])               # 세 번째 칸의 최소값
    ]

print(max(maxDP), min(minDP))
