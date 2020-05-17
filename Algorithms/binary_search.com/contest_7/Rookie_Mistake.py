class Solution:
    def solve(self, s):
        i = s.index('R')
        return 'B' not in s[:i] or 'B' not in s[i + 1:]