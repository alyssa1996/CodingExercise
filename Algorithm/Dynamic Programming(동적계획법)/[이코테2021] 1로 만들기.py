n=int(input())
dp=[0]*30001

for i in range(2,n+1):
    a,b,c=(30000,30000,30000)
    if i%5==0:
        a=dp[i//5]
    if i%3==0:
        b=dp[i//3]
    if i%2==0:
        c=dp[i//2]
    d=dp[i-1]
    dp[i]=min(a,b,c,d)+1

print(dp[n])
    
