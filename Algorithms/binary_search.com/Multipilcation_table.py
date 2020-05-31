class Solution:
    def solve(self, n):
        # Write your code here
        return [list(range(k, k*n + 1, k)) for k in range(1, n + 1)]