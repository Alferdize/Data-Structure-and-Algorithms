class Solution:
    def solve(self, n):
        ans=""
        while n:
            n,rem = divmod(n-1,26)
            ans+=chr(rem+ord("A"))
        return ans[::-1]