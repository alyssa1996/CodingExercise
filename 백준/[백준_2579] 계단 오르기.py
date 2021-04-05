n=int(input())
ar=[0]*(n+1)
dp=[0]*(n+1)

for i in range(1,n+1):
    ar[i]=int(input())

dp[1]=ar[1]
for i in range(2,n+1):
    dp[i]=max(ar[i]+ar[i-1]+dp[i-3],ar[i]+dp[i-2])

print(dp[n])
