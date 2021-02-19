tc=int(input())
for i in range(tc):
    k=int(input())
    n=int(input())
    dp=[[x for x in range(1,n+1)]]
    for j in range(k):
        dp.append([])
        for y in range(n):
            dp[-1].append(sum(dp[-2][:y+1]))
    print(dp[k][n-1])
