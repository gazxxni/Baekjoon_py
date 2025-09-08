import sys

a = list(input())
b = list(input())

lcs = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):  
    for j in range(1, len(b) + 1):  
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

i, j = len(a), len(b)
lcs_chars = []

while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
        lcs_chars.append(a[i-1])
        i -= 1; j -= 1

    else:
        if lcs[i-1][j] >= lcs[i][j-1]:
            i -= 1
        else:
            j -= 1

ans = ''.join(reversed(lcs_chars))

print(lcs[len(a)][len(b)])
print(ans)