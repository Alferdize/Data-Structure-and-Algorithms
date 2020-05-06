class Solution:
    def solve(self, matrix):
        R, C = len(matrix), len(matrix[0])
        
        def fix(sr, sc):
            # Sort the diagonal starting at (sr, sc)
            vals = []
            r, c = sr, sc
            while r < R and c < C:
                vals.append(matrix[r][c])
                r += 1
                c += 1
            
            vals.sort()
            for i, v in enumerate(vals):
                matrix[sr + i][sc + i] = v
            
        for r in range(R):
            fix(r, 0)
        for c in range(1, C):
            fix(0, c)
        return matrix