from collections import defaultdict
class Solution:
    def solve(self, matrix):
        rows = defaultdict(lambda: defaultdict(int))
        cols = defaultdict(lambda: defaultdict(int))
        squares = defaultdict(lambda: defaultdict(int))
   
        for row in range(9):
            for col in range(9):
                if not check(matrix, rows, cols, squares, row, col):
                    return False
                mark_as_visited(matrix, rows, cols, squares, row, col)
        return True
       
def check(matrix, rows, cols, squares, row, col):
    val = matrix[row][col]
    state = {
        rows[row][val],
        cols[col][val],
        squares[row//3,col//3][val],
    }
    return len(state) == 1
   
def mark_as_visited(matrix, rows, cols, squares, row, col):
    val = matrix[row][col]
    rows[row][val] = 1
    cols[col][val] = 1
    squares[row//3,col//3][val] = 1