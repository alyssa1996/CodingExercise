def solution(n):
    dp = [0, 1, 2]
    for idx in range(3, n+1):
        dp.append((dp[idx-1] + dp[idx-2]) % 1_234_567)
    return dp[n]
