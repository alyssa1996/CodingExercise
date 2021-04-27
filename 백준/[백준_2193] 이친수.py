n = int(input())
dp = [1,1,2]
for idx in range(2,91):
    dp.append(dp[-1]+dp[-2])

print(dp[n-1])
