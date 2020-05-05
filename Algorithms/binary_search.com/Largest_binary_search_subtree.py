# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        max_size = [0]
        max_node = [None]
        def traverse(node):
            if not node:
                return []
            
            left = traverse(node.left)
            right = traverse(node.right)
            
            lst = left + [node.val] + right
            if sorted(lst) == lst:
                if max_size[0] < len(lst):
                    max_size[0] = len(lst)
                    max_node[0] = node
            
            return lst
        
        traverse(root)
        return max_node[0]