class Solution:
    def solve(self, nums):
        if nums == []:
            return 1
        top_int = max(nums)
        if top_int < 1:
            return 1
        
        for i in range(1, top_int):
            if i not in nums:
                return i
        else:
            return top_int + 1