class Solution:
    def solve(self, s):
        a = s.count('A')
        b = 0
        ans = a+b
        for c in s:
            if c == 'A':
                a -= 1
            else:
                b += 1
            ans = min(ans, a+b)
        return ans