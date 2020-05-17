from math import gcd
class Solution:
    def solve(self, a, b):
        if gcd(a, b) != 1:
            return 0
        for d in [-1, 1]:
            if gcd(a+d, b) != 1 or gcd(a, b+d) != 1:
                return 1
        return 2