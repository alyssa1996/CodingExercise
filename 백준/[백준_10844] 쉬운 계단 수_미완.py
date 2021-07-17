n = int(input())
MN = 1_000_000_000
dp = [0]*101
dp[1] = 9

for idx in range(2, n+1):
    dp[idx] = ((2*dp[idx-1]) - 2**(idx-2))%MN

print(dp[n])
    
