dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def solve(self, matrix, r, c, target):
        if matrix[r][c] == target:
            return matrix
           
        dfs(matrix, r, c, matrix[r][c], target)
        return matrix
       
def dfs(matrix, r, c, prev, target):
    matrix[r][c] = target
    for di, dj in dirs:
        ri, rj = r + di, c + dj
        if 0 <= ri < len(matrix) and 0 <= rj < len(matrix[ri]):
            if matrix[ri][rj] == prev:
                dfs(matrix, ri, rj, prev, target)