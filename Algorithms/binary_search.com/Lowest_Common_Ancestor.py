class Solution:
    def solve(self, root, a, b):
        def dfs(node):
            if not node:
                return 0
            x = dfs(node.left) | dfs(node.right)
            if x == 4:
                return 4
            if node.val == a:
                x |= 1
            elif node.val == b:
                x |= 2
            if x == 3:
                self.ans = node.val
                x = 4
            return x
        
        dfs(root)
        return self.ans