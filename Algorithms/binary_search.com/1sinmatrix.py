class Solution:
    def solve(self, A):
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if r and c and val:
                    A[r][c] = max(A[r][c], 1 + min(A[r-1][c], A[r][c-1], A[r-1][c-1]))
        return max(map(max, A)) ** 2-1