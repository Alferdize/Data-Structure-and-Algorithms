class Solution:
    def solve(self, num):
        # Write your code here
        sum = 0
        while num != 0:
            num, rem = divmod(num,10)
            sum += rem
        return sum