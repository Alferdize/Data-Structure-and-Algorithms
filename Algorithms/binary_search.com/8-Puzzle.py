from collections import deque


class Solution:
    def solve(self, board):
        def neighbours(node):
            i = node.index(0)
            moves = []
            r, c = divmod(i, 3)
            if r > 0:
                moves.append(i - 3)
            if r < 2:
                moves.append(i + 3)
            if c > 0:
                moves.append(i - 1)
            if c < 2:
                moves.append(i + 1)
            arr = list(node)
            for j in moves:
                arr[i], arr[j] = arr[j], arr[i]
                yield tuple(arr)
                arr[i], arr[j] = arr[j], arr[i]

        source = tuple(board[0] + board[1] + board[2])
        target = tuple(range(9))
        seen = {source}
        queue = deque([(source, 0)])
        while queue:
            node, d = queue.popleft()
            if node == target:
                return d
            for nei in neighbours(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))
        return -1
