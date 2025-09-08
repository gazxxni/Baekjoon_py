e, s, m = map(int, input().split())
i = 1

if e == s and s == m:
    print(e)

else:
    i = 1
    while True:
        if ((i - 1) % 15 + 1 == e and
            (i - 1) % 28 + 1 == s and
            (i - 1) % 19 + 1 == m):
            print(i)

            break
        i += 1

        