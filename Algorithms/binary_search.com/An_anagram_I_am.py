import math
class Solution:
    def solve(self, s0, s1):
        f = lambda x: math.prod(ord(v) for v in x)
        return f(s0) == f(s1)