class Solution:
    def solve(self, n):
        # Write your code here
        ans=""
        while n:
            n-=1
            ans+=chr(n%26+ord("A"))
            n//=26
        return ans[::-1]