import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

dp = [[value] for value in a]
loc = 0

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            if len(dp[i]) < len(dp[j])+1:
                dp[i] = dp[j]+[a[i]]
    if len(dp[loc]) < len(dp[i]):
        loc = i

print(len(dp[loc]))
print(' '.join(map(str, dp[loc])))
