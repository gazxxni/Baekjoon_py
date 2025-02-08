import sys
input = sys.stdin.readline  
sys.setrecursionlimit(10 ** 5)

h = []

while True:
    try:
        h.append(int(input())) 
    except:
        break  

def search(st, ed):
    if st > ed:  # 시작 인덱스가 끝 인덱스를 넘어가면 종료 (기저 조건)
        return
    
    mid = ed + 1  # 오른쪽 서브트리가 없을 경우 대비비

    # 루트 노드보다 큰 첫 번째 값을 찾기 위해 반복
    for i in range(st + 1, ed + 1):
        if h[i] > h[st]:  # 현재 루트(h[st])보다 큰 값을 찾으면
            mid = i  # 오른쪽 서브트리의 시작 위치를 갱신
            break 
    
    # 왼쪽 서브트리 탐색 (현재 루트의 다음 값부터 mid - 1까지)
    search(st + 1, mid - 1)
    # 오른쪽 서브트리 탐색 (mid부터 ed까지)
    search(mid, ed)
    # 현재 루트 노드 출력
    print(h[st])

search(0, len(h) - 1)
