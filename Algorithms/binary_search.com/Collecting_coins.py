class Solution:
    def solve(self, matrix):
        # Write your code here
        rows = len(matrix)
        columns = len(matrix[0])
        for c in range(1, columns):
            matrix[0][c] += matrix[0][c-1]
        for r in range(1,rows):
            matrix[r][0] += matrix[r-1][0]
            for c in range(1,columns):
                if matrix[r-1][c] > matrix[r][c-1]:
                    matrix[r][c] += matrix[r-1][c]
                else:
                    matrix[r][c] += matrix[r][c-1]
        return matrix[-1][-1]