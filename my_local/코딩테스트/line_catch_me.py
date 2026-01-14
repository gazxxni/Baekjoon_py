from collections import deque

def solve():
    # 코니의 시작 위치와 브라운의 시작 위치를 입력받습니다.
    c_pos = int(input())
    b_pos = int(input())

    # 위치의 최대 범위를 상수로 설정합니다.
    MAX_POS = 200000
    # visited[위치][시간의 홀짝]을 기록하기 위한 2차원 리스트입니다.
    # 브라운이 특정 위치에 짝수 초에 도달했는지, 홀수 초에 도달했는지를 저장합니다.
    visited = [[False] * 2 for _ in range(MAX_POS + 1)]

    # 브라운의 이동을 추적하기 위한 큐를 생성합니다.
    queue = deque([b_pos])
    # 시작 시점인 0초(짝수)에 브라운의 위치를 방문 처리합니다.
    visited[b_pos][0] = True
    
    time = 0
    while True:
        # 매 초마다 코니의 이동 거리만큼 현재 위치를 갱신합니다.
        c_pos += time
        
        # 코니가 가동 범위를 벗어나면 브라운은 코니를 잡을 수 없습니다.
        if c_pos > MAX_POS:
            print(-1)
            break
        
        # 현재 시간의 홀짝성(0 또는 1)을 계산합니다.
        # 브라운이 이미 해당 위치에 같은 홀짝 시간에 도착해 있었다면 만남이 성사됩니다.
        if visited[c_pos][time % 2]:
            print(time)
            break
            
        # 다음 초에 이동할 위치를 계산하기 위해 현재 큐에 쌓인 데이터만큼 반복합니다.
        # 이는 BFS의 탐색 수준(Level)을 시간 단위로 구분하기 위함입니다.
        for _ in range(len(queue)):
            curr_pos = queue.popleft()
            # 다음 이동 시간의 홀짝성을 미리 계산합니다.
            next_time_parity = (time + 1) % 2
            
            # 브라운이 움직일 수 있는 세 가지 경우의 수를 확인합니다.
            for next_pos in [curr_pos - 1, curr_pos + 1, curr_pos * 2]:
                # 이동할 위치가 범위 내에 있고 아직 해당 홀짝 시간에 방문하지 않았다면 탐색을 계속합니다.
                if 0 <= next_pos <= MAX_POS and not visited[next_pos][next_time_parity]:
                    visited[next_pos][next_time_parity] = True
                    queue.append(next_pos)
        
        # 1초를 증가시켜 다음 단계로 넘어갑니다.
        time += 1

solve()