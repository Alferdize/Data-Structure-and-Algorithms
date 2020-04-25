class Solution:
    def solve(self, points, chances, k):

        n = len(points)
        xp = list(sorted(zip(points, chances)))[::-1]

        from functools import lru_cache
        
        @lru_cache(None)
        def f(i, m):
            if i >= n or m >= k:
                return 0.0
            x, p = xp[i]
            p *= 0.01
            ans = max(f(i+1, m), p*x + (1.0-p)*f(i+1, m+1))
           
            return ans
        
        return int(f(0, 0))


"""
Testcase
Input

points = [1000, 300, 10000]
chances = [20, 100, 1]
k = 2
Output

440
"""