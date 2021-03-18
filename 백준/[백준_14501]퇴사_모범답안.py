n=int(input())
t=[]
p=[]
dp=[0]*(n+1)
max_profit=0

for i in range(n):
    tc,pc=map(int,input().split())
    t.append(tc)
    p.append(pc)

for i in range(n-1,-1,-1):
    time=t[i]+i
    if time<=n:
        dp[i]=max(p[i]+dp[t[i]+i],max_profit)
        max_profit=dp[i]
    else:
        dp[i]=max_profit

print(max_profit)
