class Solution:
    def solve(self, n):
        # Write your code here
        from math import factorial, exp
        return round(factorial(n)/ exp(1))