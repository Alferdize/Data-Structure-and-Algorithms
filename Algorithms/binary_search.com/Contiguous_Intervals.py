class Solution:
    def solve(self, nums):
        nums.sort()
        nums.append(1e9)
        ans=[]
        l=nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                ans.append([l, nums[i-1]])
                l=nums[i]
        return ans