class Solution:
    def solve(self, nums):
        n = len(nums)
        ans = 0
        j = k = 0
        for i in range(n):
            j = max(j, i + nums[i])
            if k == i < n-1:
                ans += 1
                k = j
        return ans