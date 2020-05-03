class Solution:
    def solve(self, nums):
        # Write your code here
        from itertools import combinations as comb
        return max(x*y for x,y in comb(nums,2))