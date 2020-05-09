class Solution:
    def solve(self, words):
        # Write your code here
        ml = 0
        l = 0
        c = ""
        for w in words:
            f = w[0]
            if f == c:
                l += 1
            else:
                ml = max(ml,l)
                l = 1
                c = f
        ml = max(ml,l)
        return ml