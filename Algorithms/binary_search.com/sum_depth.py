# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        from collections import deque
        d = deque([(root, 1)])
        nodes = 0
        while d:
            node, depth = d.popleft()
            nodes += 1
           
            if node.left:
                d.append((node.left, 2* depth))
            if node.right:
                d.append((node.right, 2 * depth + 1))
               
        return nodes == depth