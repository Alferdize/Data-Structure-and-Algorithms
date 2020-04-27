class Solution:
    def solve(self, nums):
        # Write your code here
        smallest = nums[0]
        N = len(nums)
        tmp = 0
        for i in range(1,N):
            temp = nums[i]
            nums[i] = smallest
            if temp < smallest:
                smallest = temp
        nums[0] = 0
        return nums