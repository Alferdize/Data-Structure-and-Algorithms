class Solution:
    def solve(self, n):
        return n * n - 2 * n + (n & 1)
        
        
        # return n*n - 2 * n + (n%2)
