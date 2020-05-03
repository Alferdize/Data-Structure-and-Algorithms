from collections import Counter
class Solution:
    def solve(self,s):
        t = Counter(s)
        return min(t[c]// (1+ (c == 'z')) for c in "pizza")