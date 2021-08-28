n = int(input())

dp = [ num for num in range(n+1) ]
for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        candidate = dp[i-j*j]+1
        if dp[i] > candidate:
            dp[i] = candidate

print(dp[n])
