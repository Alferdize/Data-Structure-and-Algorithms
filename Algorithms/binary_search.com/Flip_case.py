class Solution:
    def solve(self, s):
        def swap(c):
            return c.upper() if c.islower() else c.lower()
        return "".join(map(swap, s))