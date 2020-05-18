from collections import Counter
class Solution:
    def solve(self, s, t):
        count = Counter(s) & Counter(t)
        return sum(count.values())