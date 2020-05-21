class Solution:
    def solve(self, nums, k):
        from collections import Counter
        return max(Counter(nums).values()) * k <= len(nums)