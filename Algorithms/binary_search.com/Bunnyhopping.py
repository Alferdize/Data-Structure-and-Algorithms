class Solution:
    def solve(self, nums, k):
        costs = [-1] * len(nums)
        costs[-1] = nums[-1]
        queue = [nums[-1]]
        min_cost = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            costs[i] = nums[i] + min_cost
            if costs[i] < min_cost:
                min_cost = costs[i]
            elif (i + k) < len(costs) and costs[i + k] == min_cost:
                min_cost = min(costs[i:i+k])
        return costs[0]