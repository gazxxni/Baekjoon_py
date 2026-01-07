n = int(input())
f = int(input())

base_n = (n // 100) * 100

for i in range(100):
    if (base_n + i) % f == 0:
        print(f"{i:02d}")
        break