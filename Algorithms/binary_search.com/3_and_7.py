class Solution:
    def solve(self, n):
        # Write your code here
        return (
            n % 3 == 0 or 
            n >= 7 and (n - 7) % 3 == 0 or
            n >= 14 and (n - 14) % 3 == 0
        )


        # return n >= 12 or n in [3, 6, 7, 9, 10, 12]