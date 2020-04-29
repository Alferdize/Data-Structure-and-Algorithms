from collections import Counter
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        
        def dfs(node):
            if not node: return 0
            total = dfs(node.left) + dfs(node.right) + node.val
            count[total] += 1
            return total
            
        count = Counter()
        dfs(root)
        return max(count, key=count.get)