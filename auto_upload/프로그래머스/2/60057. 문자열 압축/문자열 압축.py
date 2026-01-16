def solution(s):
    n = len(s)
    ans = n
    
    for i in range(1, n // 2 + 1):
        new = ""
        prev = s[:i]
        cnt = 1

        for j in range(i, n, i):
            cur = s[j : j + i]

            if prev == cur:
                cnt += 1
            else:
                if cnt > 1:
                    new += str(cnt) + prev
                else:
                    new += prev
                prev = cur
                cnt = 1
        
        if cnt > 1:
            new += str(cnt) + prev
        else:
            new += prev
        
        ans = min(ans, len(new))

    return ans