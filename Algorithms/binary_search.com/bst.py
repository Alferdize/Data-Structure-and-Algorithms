class Solution:
    def solve(self, root):
        # Write your code here
        return self.recurse(root)
        
    def recurse(self, root, left=float('-inf'), right=float('inf')):
        if not root:
            return True
        
        if left >= root.val or root.val >= right:
            return False
            
        if not self.recurse(root.left, left, root.val):
            return False
        
        if not self.recurse(root.right, root.val, right):
            return False
            
        return True
