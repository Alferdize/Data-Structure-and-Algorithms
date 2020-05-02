class Solution:
    def solve(self, nums):
       
# Write your code here
        nums.sort()
        curr = 1
        mx = 0
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                curr += 1
                mx = max(mx, curr)
            else:
                curr = 1
        return mx