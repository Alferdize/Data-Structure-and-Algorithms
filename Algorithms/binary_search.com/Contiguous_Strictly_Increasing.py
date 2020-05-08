class Solution:
    def solve(self, nums):
        N = len(nums)
        prefix = [1] * N
        for i in range(1,N - 1):
            if nums[i] > nums[i - 1]:
                prefix[i] = prefix[i - 1] +1
        suffix = [1] * N
        for i in range(N - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                suffix[i] = suffix[i + 1] + 1
        ans = max(max(prefix),max(suffix))
        for i in range(1, N - 1):
            if nums[i - 1] < nums[i + 1]:
                ans = max(ans, prefix[i - 1] + suffix[i + 1])
        return ans