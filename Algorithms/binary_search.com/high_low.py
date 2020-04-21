class Solution:
    count = 0
    def solve(self, root, lo, hi):
        # Write your code here
       
        if lo<=root.val<=hi:
            self.count += 1
       
        if not root.val<=lo and root.left:   self.solve(root.left, lo, hi)
        if not root.val>=hi and root.right:  self.solve(root.right, lo, hi)