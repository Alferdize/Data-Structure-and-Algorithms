class Solution:
    def solve(self, s):
        # Write your code here
        seen = set()
        for i, v in enumerate(s):
            if v in seen: return i
            seen.add(v)
        return -1