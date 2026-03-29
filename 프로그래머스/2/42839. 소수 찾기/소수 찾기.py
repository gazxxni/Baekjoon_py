from itertools import permutations

def is_prime(x):
    prime = [True] * (x + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i*i, x+1, i):
                prime[j] = False
                
    return prime

def solution(numbers):
    numbers = [int(i) for i in numbers]
    numbers.sort(reverse=True)
    m = ''.join(map(str, numbers))
    prime = is_prime(int(m))
    
    num = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num.add(int(''.join(map(str, p))))
            
    cnt = 0
    for i in list(num):
        if prime[i]:
            cnt += 1
            
    return cnt