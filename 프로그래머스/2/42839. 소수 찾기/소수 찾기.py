from itertools import permutations

def is_prime(x):
    prime = [True] * (x + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False
                
    return prime
    
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    m = ''.join(numbers)
    prime = is_prime(int(m))
    
    per = []
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            per.append(p)
    
    new = set()
    for p in per:
        new.add(int(''.join(p)))
        
    cnt = 0
    for i in list(new):
        if prime[i]:
            cnt += 1
    
    return cnt