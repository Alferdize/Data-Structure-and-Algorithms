class Solution:
    def solve(self, n):
        if n == 0:
            return 1
        if n <= 2:
            return n
            
        board = [1] * (n + 1)
        board[2] = 2
        for i in range(3, n + 1):
            board[i] = (2 * board[i-1]) + board[i-3]
            board[i] %= (10 ** 9) + 7
        return board[-1]