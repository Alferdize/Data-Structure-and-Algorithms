# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, k):
        while True:
            if root.left.val == k:
                return root.right.val
            if root.right.val == k:
                return root.left.val
            if root.val > k:
                root = root.left
            elif root.val < k:
                root = root.right