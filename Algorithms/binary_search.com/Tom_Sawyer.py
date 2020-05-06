class Solution:
    def solve(self, matrix):
        # Write your code here
        dp = matrix.pop(0)
        for row in matrix:
            m1 = min(dp)
            i1 = dp.index(m1)
            m2 = float('inf')
            for i in range(len(dp)):
                if i != i1:
                    if dp[i] < m2:
                        m2 = dp[i]
                        i2 = i
                        
            for i, x in enumerate(row):
                dp[i] = x + (m1 if i != i1 else m2)
                
        return min(dp)