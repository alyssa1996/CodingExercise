def findMax(dp,row):
    
    dp[0][1]+=dp[1][0]
    dp[1][1]+=dp[0][0]

    for i in range(2,row):
        dp[0][i]+=max(dp[1][i-1],dp[0][i-2],dp[1][i-2])
        dp[1][i]+=max(dp[0][i-1],dp[0][i-2],dp[1][i-2])

    return max(dp[0][row-1],dp[1][row-1])
            

n=int(input())

for i in range(n):
    row=int(input())
    dp=list()
    dp.append(list(map(int,input().split())))
    dp.append(list(map(int,input().split())))
    print(findMax(dp,row))
