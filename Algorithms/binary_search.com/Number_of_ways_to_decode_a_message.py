from functools import lru_cache
class Solution:
    def solve(self, message):
        # Write your code here
        @lru_cache(None)
        def dp(i):
            if i >= len(message):
                return 1
            ans = dp(i+1)
            if i < len(message)-1 and 1 <= int(message[i:i+2]) <= 26:
                ans += dp(i+2)
            return ans
        return dp(0)