n=int(input())
cards=list(map(int,input().split()))

dp=[0]*(n+1)
dp[1]=cards[0]
for i in range(1,len(cards)+1):
    for j in range(1,i):
        dp[i]=max(dp[i],dp[j]+dp[i-j])
    dp[i]=max(dp[i],cards[i-1])

print(dp[n])
