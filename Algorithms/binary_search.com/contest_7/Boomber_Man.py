class Solution:
    def solve(self, matrix):
        # Write your code here
        row = sum(1 for i in matrix if 1 not in i)
        col = sum(1 for i in zip(*matrix) if 1 not in i)
        return row*col