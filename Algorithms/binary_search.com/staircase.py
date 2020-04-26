class Solution:
    def solve(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        for x in range(1, n+1):
            dp[x]= dp[x-1] + dp[x-2]
        return dp[n]