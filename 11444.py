from functools import cache

mod = 1000000007

@cache
def fib(n):
    if n <= 2:
        return 1
    elif n % 2 == 0:
        return (fib(n//2) * (2 * fib(n // 2 - 1) + fib(n // 2))) % mod
    else:
        return (fib(n // 2 + 1) ** 2 + fib(n // 2) ** 2) % mod
    
print(fib(int(input())))