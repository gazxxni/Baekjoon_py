from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, k):
    # 방문 배열을 선언하고 -1로 초기화
    max_limit = 100001
    visited = [-1] * max_limit
    queue = deque([n])
    visited[n] = 0  # 시작점의 시간은 0

    while queue:
        current = queue.popleft()
        
        # 동생 위치에 도착하면 시간 반환
        if current == k:
            return visited[current]
        
        # 가능한 다음 이동 위치들
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < max_limit and visited[next_pos] == -1:
                if next_pos == current * 2:
                    visited[next_pos] = visited[current]
                    queue.appendleft(next_pos)
                    # 가중치가 0, 1이기 때문에 
                    # 0인 부분을 먼저 처리해야하므로 큐 앞에 넣음
                else:
                    visited[next_pos] = visited[current] + 1
                    queue.append(next_pos)

n, k = map(int, input().split())
print(bfs(n, k))
