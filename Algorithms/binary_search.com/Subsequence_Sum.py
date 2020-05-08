from collections import defaultdict
class Solution:
    def solve(self, nums):
        # Write your code here
        d = defaultdict(int)
        for i, x in enumerate(nums):
            d[x-i] +=x
        return max(d.values())
        