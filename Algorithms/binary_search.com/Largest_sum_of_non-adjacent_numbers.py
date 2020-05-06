class Solution:
    def solve(self, nums):
        # Write your code here
        N = len(nums)
        max_num = [0] * N
        max_num[0] = nums[0]
        max_num[1] = max(nums[0],nums[1])
        for i in range(2,N):
            max_num[i] = max(max_num[i-2] + nums[i], max_num[i-1], 0)
        return max_num[-1]