from functools import lru_cache
cache = {}
class Solution:
    def __init__(self):
        self.cache = cache
    def solve(self, k):
        if k <= 1: return 1
        if k in self.cache:
            return self.cache[k]
        self.cache[k] = sum((self.solve(n) * self.solve(k-n-1)) % (10**9+7) for n in range(0,k)) % (10**9+7)
        return self.cache[k]
s = Solution()
for i in range(1200):
    s.solve(i)