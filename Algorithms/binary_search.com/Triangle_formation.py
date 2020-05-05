class Solution:
    def solve(self, a, b, c):
        return a + b + c - max(a, b, c) > max(a, b, c)