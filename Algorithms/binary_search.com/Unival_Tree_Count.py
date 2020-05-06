# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        return count_unival_trees(root)

def count_unival_trees(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif root.left and root.right:
        cnt = 0
        if root.val == root.right.val and root.val == root.left.val:
            cnt = 1
        return cnt + count_unival_trees(root.left) + count_unival_trees(root.right)
    elif root.left:
        cnt = 0
        if root.val == root.left.val:
            cnt = 1
        return cnt + count_unival_trees(root.left) 
    else:
        cnt = 0
        if root.val == root.right.val:
            cnt = 1
        return cnt + count_unival_trees(root.right) 