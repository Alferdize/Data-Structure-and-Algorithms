class Solution:
    def solve(self, n):
        return bin(n).count('1') == 1
        # return n > 0 and (n & (n-1)) == 0


