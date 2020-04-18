class Solution:
    def solve(self, nums):
        n = len(nums)
        make_from_here = [False for _ in range(n)]
        make_from_here[n-1] = True
        for i in range(n-2, -1, -1):
            make_from_here[i] = any(make_from_here[i+1:i+nums[i]+1])
        return make_from_here[0]