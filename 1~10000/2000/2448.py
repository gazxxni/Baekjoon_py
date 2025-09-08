import sys
input = sys.stdin.readline

n = int(input())

def draw_star(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    
    # 재귀 호출: n/2 크기의 별 패턴을 가져옵니다.
    prev = draw_star(n // 2)
    
    # 윗부분: 이전 패턴의 각 행 앞뒤에 n/2 개의 공백을 추가하여 중앙 정렬합니다.
    top = [(" " * (n // 2)) + line + (" " * (n // 2)) for line in prev]
    
    # 아랫부분: 이전 패턴의 각 행을 좌우로 붙입니다.
    bottom = [line + " " + line for line in prev]
    
    # 윗부분과 아랫부분을 합쳐서 현재 크기의 별 패턴을 완성합니다.
    return top + bottom

result = draw_star(n)
for line in result:
    print(line)