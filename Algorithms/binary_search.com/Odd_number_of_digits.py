from math import log
class Solution:
    def solve(self, nums):
        return sum(1 for n in nums if not int(log(n,10))&1)nbvhg