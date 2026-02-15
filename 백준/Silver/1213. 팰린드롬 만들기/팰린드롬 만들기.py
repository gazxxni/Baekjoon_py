s = input().strip()
alpha_cnt = [0] * 26

for char in s:
    alpha_cnt[ord(char) - ord('A')] += 1

odd_cnt = 0
mid = ''
front = ''

for i in range(26):
    if alpha_cnt[i] % 2 == 1:
        odd_cnt += 1
        mid = chr(i + ord('A'))
    front += chr(i + ord('A')) * (alpha_cnt[i] // 2)

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(front + mid + front[::-1])