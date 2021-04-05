import sys
n=int(input())
dp=[]

for i in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    dp.append(line)

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            continue
        up,left=5000,5000
        if i-1>=0 and j>=0:
            up=dp[i-1][j]
        if i>=0 and j-1>=0:
            left=dp[i][j-1]
        dp[i][j]=min(up,left)+dp[i][j]

print(dp[n-1][n-1])
