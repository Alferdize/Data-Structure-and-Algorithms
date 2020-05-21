class Solution:
    def solve(self, matrix):
        def dfs(i, j):
            if lengths[i][j] != 0:
                return lengths[i][j]
            
            val = matrix[i][j]
            lengths[i][j] = 1 + max(
                dfs(i - 1, j) if i > 0 and matrix[i-1][j] > val else 0,
                dfs(i + 1, j) if i < m - 1 and matrix[i+1][j] > val else 0,
                dfs(i, j + 1) if j < n - 1 and matrix[i][j + 1] > val else 0,
                dfs(i, j - 1) if j > 0 and matrix[i][j - 1] > val else 0)
            return lengths[i][j]
    
    
        if not matrix:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        lengths = [[0] * n for _ in range(m)]
        return max(dfs(i, j) for i in range(m) for j in range(n))