from collections import deque 
 
t = int(input())
 
for i in range(t):
    p = input() 
    n = int(input()) 
    arr = input()[1:-1].split(',') 
 
    queue = deque(arr)  
 
    flag = 0  # 뒤집힌 횟수를 추적하는 변수 (R이 짝수면 원래 상태)
 
    if n == 0: 
        queue = []
 
    for j in p: 
        if j == 'R':  
            flag += 1  # 뒤집힌 횟수 추가
        elif j == 'D':  
            if len(queue) == 0:
                print("error")  
                break 
            else:
                if flag % 2 == 0:  # 뒤집힌 횟수가 짝수면 (정방향)
                    queue.popleft()  
                else:  # 뒤집힌 횟수가 홀수면 (뒤집힌 상태)
                    queue.pop() 
 
    else:  # 명령어 처리가 끝난 후
        if flag % 2 == 0: 
            print("[" + ",".join(queue) + "]")  # 원래 순서대로 출력
        else:  
            queue.reverse()  # deque를 뒤집어서 원래 순서대로 되돌림
            print("[" + ",".join(queue) + "]")  # 뒤집힌 결과 출력
