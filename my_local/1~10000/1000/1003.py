import sys

# t=int(input())

# def fibonacci(n):
#     global cnt0, cnt1
#     if n==0:
#         cnt0+=1
#         return 0
#     elif n==1:
#         cnt1+=1
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# for _ in range(t):
#     cnt0=0
#     cnt1=0
#     fibonacci(int(input()))
#     print(cnt0,cnt1)


t = int(input())

for _ in range(t):
    n = int(input())

    dp = [[]]*41
    dp[0] = [1,0]
    dp[1] = [0,1]
    dp[2] = [1,1]

    for i in range(3, n+1):
        dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]

    print(dp[n][0], dp[n][1])
