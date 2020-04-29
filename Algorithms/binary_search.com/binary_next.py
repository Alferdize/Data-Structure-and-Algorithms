class Solution:
    def solve(self, n):
        # Write your code here
        copy = n
        ones,zeros = 0,0
        while copy and not copy & 1:
            zeros += 1
            copy >>= 1
        while copy & 1:
            ones += 1
            copy >>= 1
        right = ones + zeros
        n |= 1 << right
        n &= ~((1 << right)-1)
        n |= ((1 << ones-1) -1)
        return n
        