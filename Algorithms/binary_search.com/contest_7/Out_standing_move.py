class Solution:
    def solve(self, nums):
        orig = compute(nums)
        off = 0
        for i,n in enumerate(nums):
            cur = 0
            for j in range(i+1, len(nums)):
                cur += n
                cur -= nums[j]
                off = max(off, cur)
                
        for i,n in enumerate(nums):
            cur = 0
            for j in range(i-1, -1, -1):
                cur -= n
                cur += nums[j]
                off = max(off,cur)
                
        return orig + off
        
def compute(lst):
    return sum((i+1) * v for i,v in enumerate(lst))