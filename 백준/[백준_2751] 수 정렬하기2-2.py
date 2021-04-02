import sys
n=int(input())
dp=[0]*(n+1)

for i in range(n):
    number=int(sys.stdin.readline())
    dp[number]+=1

for i in range(1,n+1):
    for j in range(dp[i]):
        print(i)


