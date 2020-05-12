class Solution:
    def solve(self, nums):
        for r in range(2):
            for i in range(r, len(nums) - 2, 4):
                nums[i], nums[i+2] = nums[i+2], nums[i]
        return nums