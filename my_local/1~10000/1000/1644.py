import sys, math
input = sys.stdin.readline

n = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

primenums = []

for i in range(2, n+1):
    if is_prime(i):
        primenums.append(i)

st, ed = 0, 0
cnt = 0
total = 0

while True:
    if total >= n:
        if total == n:
            cnt += 1
        total -= primenums[st]
        st += 1
    elif ed == len(primenums):
        break
    else:
        total += primenums[ed]
        ed += 1

print(cnt)