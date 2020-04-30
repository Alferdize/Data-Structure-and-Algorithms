class Solution:
    def solve(self, matrix):
        total = 0
        n = len(matrix)
        j = n - 2
        for i in range(n):
            if i == 0 or i == n - 1:
                total += sum(matrix[i])
            else:
                total += matrix[i][j]
                j -= 1
        return total


# class Solution:
#     def solve(self, A):
#         if not A: return 0
#         return sum((
#             sum(A[0][:-1]),
#             sum(A[-1][1:]),
#             sum(A[i][-1-i] for i in range(len(A))),
#         ))