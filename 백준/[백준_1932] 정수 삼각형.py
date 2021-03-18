import sys
n=int(input())
dp=[]

for i in range(1,n+1):
    numbers=list(map(int,sys.stdin.readline().split()))
    numbers=numbers+([0]*(n-i))
    dp.append(numbers)

for i in range(1,n):
    for j in range(i+1):
        current=dp[i][j]
        dp[i][j]=dp[i-1][j]
        if i-1>=0 and j-1>=0:
            dp[i][j]=max(dp[i][j],dp[i-1][j-1])
        dp[i][j]+=current

print(max(dp[n-1]))
