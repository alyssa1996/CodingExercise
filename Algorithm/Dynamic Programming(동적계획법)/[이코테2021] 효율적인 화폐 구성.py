import sys

n,m=map(int,input().split())
value=list()
dp=[10001]*(m+1)
d=dp.copy()
for i in range(n):
    value.append(int(sys.stdin.readline()))

for i in range(1,m+1):
    for j in value:
        if i%j==0:
            dp[i]=min(dp[i],i//j)
        if i>j:
            dp[i]=min(dp[i],dp[i-j]+1)

if dp[m]>10000:
    print(-1)
else:
    print(dp[m])
 
#모범답안

d[0]=0
for i in range(n):
    for j in range(value[i],m+1):
        if d[j-value[i]]!=10001:
            d[j]=min(d[j],d[j-value[i]]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])
