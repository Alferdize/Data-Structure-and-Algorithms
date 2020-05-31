class Solution:
    def solve(self, nums):
        odds, evens = [], []
        for x in nums:
            if x % 2:
                odds.append(x)
            else:
                evens.append(x)

        odds.sort()
        evens.sort(reverse=True)
        
        for i, x in enumerate(nums):
            if x % 2:
                nums[i] = odds.pop()
            else:
                nums[i] = evens.pop()
        
        return nums