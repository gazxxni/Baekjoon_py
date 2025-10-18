import sys, heapq
from collections import defaultdict
'''
BFS로 풀면 모든 지점을 다 돌아야해서 시간초과
-> 다익스트라로 텔레포트 사용 구간만 검사, 텔레포트 안 쓰면 그냥 긴 거리가 답
'''
input = sys.stdin.readline

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

start_node = (xs, ys)
end_node = (xe, ye)

tp_dic = defaultdict(list)
tp_node = set()

for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    node1 = (x1, y1)
    node2 = (x2, y2)
    
    tp_node.add(node1)
    tp_node.add(node2)

    tp_dic[node1].append((node2, 10))
    tp_dic[node2].append((node1, 10))

key_nodes = list(tp_node)
key_nodes.append(start_node)

distances = {node: float('inf') for node in key_nodes}
distances[start_node] = 0

pq = [(0, start_node)]

# 시작점에서 도착점까지 가는 비용 (이게 기본 답)
min_cost = abs(xs - xe) + abs(ys - ye)

while pq:
    current_cost, current_node = heapq.heappop(pq)

    if current_cost > distances[current_node]:
        continue

    # 현재 위치에서 도착점까지 비용
    # (현재까지 비용 + 지금 위치에서 도착점까지 걷는 비용)
    cost_via_current = current_cost + abs(current_node[0] - end_node[0]) + abs(current_node[1] - end_node[1])
    min_cost = min(min_cost, cost_via_current)
    
    # 텔레포트 
    if current_node in tp_dic:
        for next_node, tele_cost in tp_dic[current_node]:
            new_cost = current_cost + tele_cost
            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    # 현재 위치에서 모든 텔레포트 지점까지 비용 계산
    for next_tp_node in tp_node:
        if current_node == next_tp_node:
            continue
            
        walk_cost = abs(current_node[0] - next_tp_node[0]) + abs(current_node[1] - next_tp_node[1])
        new_cost = current_cost + walk_cost
        
        if new_cost < distances[next_tp_node]:
            distances[next_tp_node] = new_cost
            heapq.heappush(pq, (new_cost, next_tp_node))

print(min_cost)