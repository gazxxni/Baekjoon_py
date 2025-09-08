import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def search(x):
    total = 0

    for i in range(64):  
        block_size = 2 ** (i + 1)  
        half_block = 2 ** i           

        full_blocks = (x + 1) // block_size
        remainder = (x + 1) % block_size

        cnt = full_blocks * half_block

        if remainder > half_block:
            cnt += remainder - half_block

        total += cnt

    return total

print(search(b) - search(a - 1))