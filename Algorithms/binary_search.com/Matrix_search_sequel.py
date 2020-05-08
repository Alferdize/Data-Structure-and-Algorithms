class Solution:
    def solve(self, matrix, target):
        # Write your code here
        if not matrix:
            return False
        
        M, N = len(matrix), len(matrix[0])
        i, j = M-1, 0
        while i >= 0 and j < N:
            if matrix[i][j] > target:
                i-=1
            elif matrix[i][j] < target:
                j +=1
            else:
                return True
        return False
