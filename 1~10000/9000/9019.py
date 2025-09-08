from collections import deque 

t = int(input().strip())

for _ in range(t):
    visited = [False] * 10001
    
    a, b = map(int, input().strip().split())

    q = deque()
    q.append([a, ''])  # 초기값으로 A와 빈 문자열 추가
    visited[a] = True  # a를 방문했음을 표시

    while q:
        n, cmd = q.popleft()
        
        if n == b:  # 목표 b가 나오면 기록 출력
            print(cmd)
            break

        # **연산 D**: 현재 숫자 * 2, 결과가 10000을 넘으면 10000으로 나눈 나머지
        d = (n * 2) % 10000
        if not visited[d]:      
            visited[d] = True       
            q.append([d, cmd + 'D'])  # 큐에 새로운 상태와 연산 기록 추가

        # **연산 S**: 현재 숫자 - 1, 결과가 음수면 9999로 변경
        s = (n - 1) % 10000
        if not visited[s]:
            visited[s] = True
            q.append([s, cmd + 'S'])

        # **연산 L**: 현재 숫자를 왼쪽으로 회전  # 1234 → 2341 (앞의 자리수를 뒤로 이동)
        l = n // 1000 + (n % 1000) * 10
        if not visited[l]:
            visited[l] = True
            q.append([l, cmd + 'L'])

        # **연산 R**: 현재 숫자를 오른쪽으로 회전  # 1234 → 4123 (뒤의 자리수를 앞으로 이동)
        r = n // 10 + (n % 10) * 1000
        if not visited[r]:
            visited[r] = True
            q.append([r, cmd + 'R'])
