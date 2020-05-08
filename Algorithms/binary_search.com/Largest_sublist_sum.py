from math import inf

class Solution:
    def solve(self, nums):
        # Write your code here
        ans = cur = -inf
        for x in nums:
            cur = max(x, cur + x)
            ans = max(ans, cur)
        return ans