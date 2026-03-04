from itertools import permutations

def solution(numbers):    
    def prime(x):
        is_prime = [True] * (x + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(x ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, x + 1, i):
                    is_prime[j] = False
        
        return [i for i in range(2, x + 1) if is_prime[i]]            
                    
        
    new_num = list(map(str, numbers))
    new_num.sort(reverse=True)
    
    max_num = ''.join(new_num)
    
    prime_num = prime(int(max_num))
    
    per = [p for i in range(1, len(new_num) + 1) for p in permutations(new_num, i)]
    
    arr = set()
    for i in per:
        arr.add(int(''.join(i)))
    
    cnt = 0
    for i in list(arr):
        if i in prime_num:
            cnt += 1
            
    return cnt