class Solution:
    def solve(self, root0, root1):
        # Write your code here
        def dfs(node0, node1):
            if not node0 or not node1:
                return False
            elif node0.val != node1.val:
                return False
            
            if node0.left and not dfs(node0.left, node1.left):
                return False
            elif node0.right and not dfs(node0.right, node1.right):
                return False
            return True 
        return dfs(root0, root1)