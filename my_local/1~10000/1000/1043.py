import sys 

n, m = map(int, input().split())
truth = set(input().split()[1:])  # 앞 1개의 원소를 빼고 저장장
party = []

for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for i in party: 
        if i & truth:  # 파티 참석자가 있고 진실을 아는 사람이 있을 때
            truth = truth.union(i)  # truth와 i의 합집합 반환환

cnt = 0

for i in party:
    if i & truth:  # 현재 파티에 진실을 아는 사람이 포함된 경우
        continue 
    cnt += 1  # 진실을 모르는 사람들이 즐길 수 있는 파티일 경우 카운트 증가

print(cnt)
