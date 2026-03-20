from collections import deque
def solution(bridge_length, weight, truck_weights):
    ans = 0
    running = deque()
    
    while truck_weights or running:
        ans += 1
        
        for i in range(len(running)):
            running[i][1] += 1
        
        if running and running[0][1] > bridge_length:
            running.popleft()
            
        if truck_weights:
            new = sum(i[0] for i in running)
            
            if new + truck_weights[0] <= weight and len(running) <= bridge_length:
                running.append([truck_weights[0], 1])
                truck_weights.pop(0)
    
    return ans