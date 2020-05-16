class Solution:
    def solve(self, n):
        # Write your code here
        a,b,c = -1,1,0
        for i in range(n+2):
            c = (a+b) % (10 ** 9 +7)
            a = b
            b = c
        return c