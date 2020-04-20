class Solution:
    def solve(self, root):
        if not root:
            return True
        return self.is_same(root.left, root.right)
        
    def is_same(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return p.val == q.val and self.is_same(p.left, q.right) and self.is_same(p.right, q.left)