from collections import defaultdict


class Solution:
    def solve(self, nums, target):
        seen = defaultdict(int)
        seen[0] = 1
        s, ans = 0, 0
        for i in range(len(nums)):
            s += nums[i]
            comp = s - target
            if comp in seen:
                ans += seen[comp]
            seen[s] += 1
        return ans
