from itertools import groupby
class Solution:
    def solve(self, s):
        m = 0
        for k,c in groupby(s):
            m = max(m,len(list(c)))
        return m