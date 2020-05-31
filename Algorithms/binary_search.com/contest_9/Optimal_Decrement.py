class Solution:
    def solve(self, nums, k):
        nums.sort(reverse=True)
        l=r=0
        while k>0:
            while r<len(nums)-1 and nums[l] == nums[r+1]:
                r+=1
            for i in range(l,r+1):
                nums[i]-=1
                k-=1
                if k ==0: break
        return max(nums)