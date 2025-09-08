import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dict = {}

for i in range(1, n+1):
    a = input().rstrip()
    dict[i] = a  # 양방향 매핑 필수
    dict[a] = i

for i in range(m):
    a = input().rstrip()

    if a.isdigit():   # 숫자로만 구성된 문자열인지 확인
        print(dict[int(a)])
    else:
        print(dict[a])