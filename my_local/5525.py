import sys

input=sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
s = input().strip()

p = 'IOI'

cnt = i = ans = 0

while i < (m - 1):   # 입력받은 S의 길이만큼 반복
    if s[i : i+3] == p:  # 현재 반복되는 문자열이 'IOI'인가 ?
        i += 2       # 그렇다면 다음에도 반복하는지 확인하기 위해 i+2
        cnt += 1     # 'IOI' 반복 수 저장
        if cnt == n:     # 반복 수 cnt가 우리가 원하는 N과 동일한가 ?
            ans += 1     # 그렇다면 Pn을 찾은 것이므로 answer + 1
            cnt -= 1     # 지금 Pn의 일부를 포함해서 또다른 Pn이 나올 수 있으므로 
                         # cnt를 초기화하지 않고 -1만 함

    else:
        i += 1    # 'IOI'가 아니면 다음 인덱스로 이동
        cnt = 0   # cnt 초기화

print(ans)
