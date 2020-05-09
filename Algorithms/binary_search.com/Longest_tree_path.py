# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        mx = 0
        def dfs(node):
            nonlocal mx
            if not node: return 0
            deepest_left = dfs(node.left)
            deepest_right = dfs(node.right)
            mx = max(mx,deepest_left+deepest_right+1)
            return 1 + max(deepest_left, deepest_right)
        dfs(root)
        return mx