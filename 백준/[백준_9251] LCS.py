a = input()
b = input()

length_a, length_b = len(a), len(b)
dp = [[0]*(length_b+1) for _ in range(length_a+1)]

for i in range(1, length_a+1):
    for j in range(1, length_b+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[length_a][length_b])
