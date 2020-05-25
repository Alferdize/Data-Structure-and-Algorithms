class Solution:
    def solve(self, nums):
        # Write your code here
        if len(nums) <=2:
            return 0
        n= len(nums)-1
        prev = nums[0]
        prev_index = 0
        water =0
        temp =0 
        for i in range(1,n+1):
            if nums[i] >= prev:
                prev = nums[i]
                prev_index = i
                temp = 0
            else:
                water += prev - nums[i]
                temp += prev - nums[i]
        if prev_index < n:
            water -= temp
            prev = nums[n]
            for i in range(n,prev_index-1,-1):
                if nums[i] >= prev:
                    prev = nums[i]
                else:
                    water += prev - nums[i]
        return water