class Solution:
    def solve(self, root):
        if not root.left and not root.right: return str(root.val)
        return "({} {} {})".format(root.val, self.solve(root.left), self.solve(root.right))