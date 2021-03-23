import sys
n=int(input())
ar=list(map(int,sys.stdin.readline().split()))

if len(ar)==1:
    print(ar[0])
else:
    dp=[0]*n
    dp[1]=ar[0]+ar[1]
    result=ar[0]

    for i in range(1,len(ar)):
        dp[i]=max(dp[i-1],ar[i-1],0)+ar[i]
        if result<dp[i]:
            result=dp[i]

    print(result)    
