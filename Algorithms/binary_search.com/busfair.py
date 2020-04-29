from functools import lru_cache
import math

info = ((1,2), (7,7), (30,25))

class Solution:
    def solve(self,A):
        @lru_cache(None)
        def dfs(day):
            if day >= len(A):
                return 0
            result = math.inf
            index = day
            for x, y in info:
                while index < len(A) and A[index] < A[day] + x:
                    index += 1
                result = min(result, dfs(index) + y)
            return result
           
        return dfs(0)