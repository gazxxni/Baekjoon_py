import sys

input = sys.stdin.readline

x = int(input())

line = 1

# 짝수 라인 : 분모가 1씩 늘어나고 분자가 1씩 줄어듦
# 홀수 라인 : 분자가 1씩 늘어나고 분모가 1씩 줄어듦
# 각 줄에 있는 항목의 개수(line)를 빼면서 x가 어느 줄에 속하는지 찾음
while x > line:
    x -= line  # 해당 줄의 수만큼 x에서 빼줌
    line += 1  # 다음 줄로 넘어감

if line % 2 == 0:
    a = x  # 분자
    b = line - x + 1  # 분모

elif line % 2 == 1:
    a = line - x + 1  # 분자
    b = x  # 분모

print(f'{a}/{b}')
