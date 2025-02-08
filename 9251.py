import sys

a = list(input())
b = list(input())

lcs = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):  # 문자열 `a`를 순회
    for j in range(1, len(b) + 1):  # 문자열 `b`를 순회
        # 두 문자가 같으면 이전 대각선 값 + 1
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            # 다르면 왼쪽 값과 위쪽 값 중 최대값을 선택
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(max(map(max, lcs)))  # 각 행의 최댓값 중 큰 값 출력
