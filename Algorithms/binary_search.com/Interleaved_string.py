from itertools import zip_longest
class Solution:
    def solve(self, s0, s1):
        return "".join(x+y for x,y in zip_longest(s0,s1,fillvalue=""))