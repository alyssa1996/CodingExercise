test=int(input())

for i in range(test):
    dp=[0,1,2,4]
    number=int(input())
    for j in range(4,number+1):
        dp.append(dp[j-1]+dp[j-2]+dp[j-3])
    print(dp[number])
