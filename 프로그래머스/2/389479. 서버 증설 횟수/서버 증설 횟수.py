def solution(players, m, k):
    servers = [0] * 24 # 증설된 서버의 수
    cnt = 0 # 증설 횟수
    
    for i in range(24):
        p = players[i] // m # 필요한 서버의 수
        
        if p > servers[i]: # 필요한 서버의 수가 증설된 서버의 수보다 크면
            diff = p - servers[i] # 증설 횟수
            cnt += diff
            
            if i + k < 24:
                for j in range(i, i+k):
                    servers[j] += diff
            else:
                for j in range(i, 24):
                    servers[j] += diff

    return cnt