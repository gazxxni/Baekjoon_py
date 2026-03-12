from itertools import product

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(1, 6):
        for p in product(alpha, repeat=i):
            arr.append("".join(p))
        
    arr.sort()
    ans = arr.index(word) + 1
    return ans