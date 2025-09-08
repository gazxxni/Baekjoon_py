import sys

t=int(input())

for _ in range(t):
    wears={}
    n=int(input())

    for _ in range(n):
        # 의상 이름과 타입을 입력받음
        name, type=sys.stdin.readline().strip().split()

        # 타입이 딕셔너리에 없으면 추가하고 1로 초기화
        if not type in wears:
            wears[type]=1
        else:
            # 타입이 이미 존재하면 개수를 증가시킴
            wears[type]+=1

    cnt=1

    for i in wears:
        # 각 타입의 의상 개수 + 1(안 입는 경우) 만큼 조합 수를 증가시킴
        cnt*=(wears[i]+1)

    print(cnt-1)

    