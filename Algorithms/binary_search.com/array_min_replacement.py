class Solution:
    def solve(self, nums):
        # Write your code here
        small = nums[0]
        temp = 0
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = small
            if small > temp:
                small =temp
        nums[0] = 0
        return nums