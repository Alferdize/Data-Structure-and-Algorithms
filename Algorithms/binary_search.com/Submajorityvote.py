from collections import Counter
class Solution:
    def solve(self, nums):
        return sorted([k for k, v in dict(Counter(nums)).items() if v > (len(nums)/3)])