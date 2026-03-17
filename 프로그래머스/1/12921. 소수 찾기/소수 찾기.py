def is_prime(x):
    prime = [True] * (x + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i*i, x + 1, i):
                prime[j] = False
                
    return prime
        
        
def solution(n):
    prime = is_prime(n)

    return prime.count(True)