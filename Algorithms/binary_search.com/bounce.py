class Solution:
    def solve(self, nums, k):
        # Write your code here
        def jump(i):
            if i == len(nums) - 1: return True
            if i < 0 or i >= len(nums): return False
            if nums[i] < 0: return False
           
            n = nums[i]
            nums[i] = -1
           
            return jump(i + n) or jump(i - n)
   
        return jump(k)