class Solution:
    def solve(self, s, k):
        inner = '.' * (2*k-1)
        outer = '.' * k
        return inner in s or s.startswith(outer) or s.endswith(outer)