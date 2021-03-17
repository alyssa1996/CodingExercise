import sys
testcase=int(input())

for i in range(testcase):
    n,m=map(int,input().split())
    dp=[]
    gold=list(map(int,sys.stdin.readline().split()))

    for j in range(n):
        dp.append(gold[j*m:(j+1)*m])

    for y in range(1,m):
        for x in range(n):
            a,b=0,0
            if x-1>0:
                a=dp[x-1][y-1]
            if x+1<n:
                b=dp[x+1][y-1]
            dp[x][y]+=max(a,b,dp[x][y-1])

    result=0
    for k in range(n):
        if result<dp[k][m-1]:
            result=dp[k][m-1]
    print(result)
