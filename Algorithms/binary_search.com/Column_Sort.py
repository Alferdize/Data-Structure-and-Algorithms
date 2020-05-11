class Solution:
    def solve(self, matrix):
        # Write your code here
        matrix = list(zip(*matrix))
        for i in range(len(matrix)):
            matrix[i] = sorted(matrix[i])
        return list(zip(*matrix))