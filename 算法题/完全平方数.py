from math import *
#动态规划，找到状态转移方程
def numSquares(n):
    dp = [0] * (n+1)
    for i in range(1,n+1):
        j = 1
        dp[i] = i
        while j**2 <= i:
            dp[i] = min(dp[i], dp[i - j ** 2] + 1)
            j += 1
    return dp[n]
#深度优先遍历
print(numSquares(13))